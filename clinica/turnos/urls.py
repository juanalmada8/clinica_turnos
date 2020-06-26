from django.urls import path
from turnos import views

urlpatterns = [
    path('', views.turnos, name='turnos')
]