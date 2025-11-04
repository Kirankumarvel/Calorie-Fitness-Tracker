import io
import base64
import matplotlib
# Use a non-interactive backend to avoid display issues
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login
from django.db.models import Sum
from .models import CalorieEntry
from .forms import CalorieEntryForm, CustomUserCreationForm

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'tracker/home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'tracker/register.html', {'form': form})

@login_required
def dashboard(request):
    today = datetime.now().date()
    
    # Today's totals
    today_food = CalorieEntry.objects.filter(
        user=request.user, 
        entry_type='food', 
        date=today
    ).aggregate(total=Sum('calories'))['total'] or 0
    
    today_exercise = CalorieEntry.objects.filter(
        user=request.user, 
        entry_type='exercise', 
        date=today
    ).aggregate(total=Sum('calories'))['total'] or 0
    
    today_net = today_food - today_exercise
    
    # Recent entries
    recent_entries = CalorieEntry.objects.filter(user=request.user)[:5]
    
    context = {
        'today_food': today_food,
        'today_exercise': today_exercise,
        'today_net': today_net,
        'recent_entries': recent_entries,
    }
    return render(request, 'tracker/dashboard.html', context)

@login_required
def add_entry(request):
    if request.method == 'POST':
        form = CalorieEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            messages.success(request, 'Entry added successfully!')
            return redirect('entries_list')
    else:
        form = CalorieEntryForm()
    return render(request, 'tracker/add_entry.html', {'form': form})

@login_required
def entries_list(request):
    entries = CalorieEntry.objects.filter(user=request.user)
    return render(request, 'tracker/entries_list.html', {'entries': entries})

@login_required
def delete_entry(request, entry_id):
    entry = get_object_or_404(CalorieEntry, id=entry_id, user=request.user)
    if request.method == 'POST':
        entry.delete()
        messages.success(request, 'Entry deleted successfully!')
    return redirect('entries_list')

@login_required
def charts(request):
    try:
        # Get data for the last 7 days
        end_date = datetime.now().date()
        start_date = end_date - timedelta(days=6)
        
        dates = []
        food_calories = []
        exercise_calories = []
        net_calories = []
        
        current_date = start_date
        while current_date <= end_date:
            dates.append(current_date.strftime('%m/%d'))
            
            food_total = CalorieEntry.objects.filter(
                user=request.user,
                entry_type='food',
                date=current_date
            ).aggregate(total=Sum('calories'))['total'] or 0
            
            exercise_total = CalorieEntry.objects.filter(
                user=request.user,
                entry_type='exercise',
                date=current_date
            ).aggregate(total=Sum('calories'))['total'] or 0
            
            food_calories.append(food_total)
            exercise_calories.append(exercise_total)
            net_calories.append(food_total - exercise_total)
            
            current_date += timedelta(days=1)
        
        # Create the chart only if we have data
        if any(food_calories) or any(exercise_calories):
            # Set style for better looking charts
            plt.style.use('default')
            
            # Create figure and axis
            fig, ax = plt.subplots(figsize=(12, 6))
            
            # Plot data
            line1 = ax.plot(dates, food_calories, marker='o', label='Food Calories', color='#3498db', linewidth=2, markersize=6)
            line2 = ax.plot(dates, exercise_calories, marker='s', label='Exercise Calories', color='#e74c3c', linewidth=2, markersize=6)
            line3 = ax.plot(dates, net_calories, marker='^', label='Net Calories', color='#27ae60', linewidth=2, markersize=6, linestyle='--')
            
            # Customize the chart
            ax.set_title('Weekly Calorie Tracking', fontsize=16, fontweight='bold', pad=20)
            ax.set_xlabel('Date', fontsize=12)
            ax.set_ylabel('Calories', fontsize=12)
            ax.legend(fontsize=10)
            ax.grid(True, alpha=0.3)
            
            # Rotate x-axis labels for better readability
            plt.xticks(rotation=45)
            
            # Adjust layout to prevent label cutoff
            plt.tight_layout()
            
            # Convert plot to PNG image
            buffer = io.BytesIO()
            plt.savefig(buffer, format='png', dpi=100, bbox_inches='tight')
            buffer.seek(0)
            image_png = buffer.getvalue()
            buffer.close()
            
            graphic = base64.b64encode(image_png)
            graphic = graphic.decode('utf-8')
            plt.close(fig)  # Explicitly close the figure to free memory
            
            chart_data = {
                'chart': graphic,
                'has_data': True,
                'dates': dates,
                'food_totals': food_calories,
                'exercise_totals': exercise_calories,
                'net_totals': net_calories
            }
        else:
            chart_data = {
                'chart': None,
                'has_data': False,
                'message': 'No data available for the past 7 days. Add some entries to see your charts!'
            }
        
        return render(request, 'tracker/charts.html', chart_data)
        
    except Exception as e:
        # Fallback in case of any errors
        print(f"Chart generation error: {e}")  # For debugging
        return render(request, 'tracker/charts.html', {
            'chart': None,
            'has_data': False,
            'message': f'Chart temporarily unavailable. Error: {str(e)}'
        })