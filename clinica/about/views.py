from django.shortcuts import render
from .models import About
# from .models import Especialidades

# Create your views here.
def about(request):
    # especialidad = Especialidades.objects.all()
    about = About.objects.all()
    return render(request, 'about/about.html', {'sobremi': about})
