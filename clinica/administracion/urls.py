from django.urls import path
from django.contrib.auth import views as auth_views
#from administracion import views
from .views import TablaTurno

urlpatterns = [
    #path('', views.tablaturnos, name='turno_list'),
    path('', TablaTurno.as_view(), name='turno_list'),
  
]