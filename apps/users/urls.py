from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('password-reset/', views.CustomPasswordResetView.as_view(), name='password_reset')
]
