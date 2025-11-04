from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_entry, name='add_entry'),
    path('entries/', views.entries_list, name='entries_list'),
    path('delete/<int:entry_id>/', views.delete_entry, name='delete_entry'),
    path('charts/', views.charts, name='charts'),
]