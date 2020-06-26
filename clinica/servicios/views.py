from django.shortcuts import render

# Create your views here.
def especialidades(request):
    return render(request, 'servicios/especialidades.html')