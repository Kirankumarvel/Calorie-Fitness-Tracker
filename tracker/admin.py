from django.contrib import admin
from .models import CalorieEntry

@admin.register(CalorieEntry)
class CalorieEntryAdmin(admin.ModelAdmin):
    list_display = ['user', 'entry_type', 'name', 'calories', 'date']
    list_filter = ['entry_type', 'date', 'user']
    search_fields = ['name', 'user__username']