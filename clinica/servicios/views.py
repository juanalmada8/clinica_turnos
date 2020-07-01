from django.shortcuts import render
from .models import Especialidades

# Create your views here.
def especialidades(request):
    especialidad = Especialidades.objects.all()
    return render(request, 'servicios/especialidades.html', {'servicio': especialidad})
