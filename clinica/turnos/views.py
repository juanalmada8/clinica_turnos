from django.shortcuts import render, redirect
from .forms import TurnosForm
from django.urls import reverse
from .models import Turno

def turnos(request):
    lista_turno = Turno.objects.all()
    turno = TurnosForm()
    if request.method == 'POST':
        turno = TurnosForm(data=request.POST)
        if turno.is_valid():
            turno.save()
            # nombre = request.POST.get('nombre', '')
            # obra_social = request.POST.get('obra_social', '')
            # email = request.POST.get('email', '')
            # edad = request.POST.get('edad', '')
            # dni = request.POST.get('dni', '')
            # telefono = request.POST.get('telefono', '')
            # direccion = request.POST.get('direccion', '')
            return redirect(reverse('turnos')+"?OK")

    return render(request, 'turnos/turnos.html', {'lista_turno':lista_turno,'turno':turno})



    