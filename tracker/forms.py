from django import forms
from .models import CalorieEntry
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CalorieEntryForm(forms.ModelForm):
    class Meta:
        model = CalorieEntry
        fields = ['entry_type', 'name', 'calories', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def clean_calories(self):
        calories = self.cleaned_data.get('calories')
        if calories <= 0:
            raise forms.ValidationError("Calories must be a positive number.")
        return calories