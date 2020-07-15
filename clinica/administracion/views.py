from django.shortcuts import render
from turnos.models import Turno
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
# Create your views here.

class TablaTurno(LoginRequiredMixin, ListView):
    model = Turno
    template_name = 'administracion/turnos.html'
    context_object_name = "turnos"
    login_url = 'login:login'



#def tablaturnos(request):
#    turnos= Turno.objects.all()
#    return render(request, 'administracion/turnos.html', {'turnos': turnos})