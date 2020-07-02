from django.shortcuts import render
from .forms import TurnosForm

# Create your views here.
def turnos(request):
    turno = TurnosForm()
    return render(request, 'turnos/turnos.html', {'turno':turno})
    