from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('pricing/', views.pricing, name='pricing'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about')
]
