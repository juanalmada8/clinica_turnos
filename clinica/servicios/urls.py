from django.urls import path
from servicios import views

urlpatterns = [
    path('', views.especialidades, name='especialidades')
]