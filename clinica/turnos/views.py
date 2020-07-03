from django.shortcuts import render, redirect
from .forms import TurnosForm
from django.urls import reverse

# Create your views here.
def turnos(request):
    turno = TurnosForm()
    if request.method == 'POST':
        turno = TurnosForm(data=request.POST)
        if turno.is_valid():
            nombre = request.POST.get('nombre', '')
            obra_social = request.POST.get('obra_social', '')
            email = request.POST.get('email', '')
            edad = request.POST.get('edad', '')
            dni = request.POST.get('dni', '')
            telefono = request.POST.get('telefono', '')
            direccion = request.POST.get('direccion', '')
            return redirect(reverse('turnos')+"?OK")

    return render(request, 'turnos/turnos.html', {'turno':turno})
    