from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from tracker import views as tracker_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tracker_views.home, name='home'),
    path('register/', tracker_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='tracker/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', tracker_views.dashboard, name='dashboard'),
    path('tracker/', include('tracker.urls')),
]