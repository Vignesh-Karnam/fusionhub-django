from django.urls import path

from . import views

app_name = 'competitors'
urlpatterns = [
    path('', views.competitors, name='competitors')
]
