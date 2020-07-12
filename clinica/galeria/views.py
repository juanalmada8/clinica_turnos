from django.shortcuts import render
# from .models import Especialidades

# Create your views here.
def galeria(request):
    # especialidad = Especialidades.objects.all()
    return render(request, 'galeria/galeria.html')
