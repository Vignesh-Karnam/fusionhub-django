from django.urls import path

from . import views

app_name = 'competitors'
urlpatterns = [
    path('', views.CompetitorsView.as_view(), name='competitors'),
    path('upload/', views.upload_competitors, name='upload')
]
