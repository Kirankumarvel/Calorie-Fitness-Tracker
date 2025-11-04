from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class CalorieEntry(models.Model):
    ENTRY_TYPES = [
        ('food', 'Food Intake'),
        ('exercise', 'Exercise'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    entry_type = models.CharField(max_length=10, choices=ENTRY_TYPES)
    name = models.CharField(max_length=200)
    calories = models.IntegerField()
    date = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date', '-created_at']
    
    def __str__(self):
        return f"{self.user.username} - {self.name} - {self.calories} cal"