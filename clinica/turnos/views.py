from django.shortcuts import render

# Create your views here.
def turnos(request):
    return render(request, 'turnos/turnos.html')