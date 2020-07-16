from django import forms
from .models import Turno

""" def retornarFecha(modelo):
    fechas = modelo.objects.all()
    lista = []
    for fecha in fechas:
        lista.append(fecha.fecha_consulta)
    return  lista
#a = FechaConsulta.objects.all() """
#fechas = [i.fecha_consulta for i in FechaConsulta.objects.all()]


class TurnosForm(forms.ModelForm):

    nombre = forms.CharField(label='Nombre y apellido',required=True, widget=forms.TextInput(
        attrs={'class':"form-control", 'placeholder': "Nombre"}))
    obra_social = forms.CharField(label='Obra Social',required=True, widget=forms.TextInput(
        attrs={'class':"form-control", 'placeholder': "Obra Social"}))
    email = forms.EmailField(label='Email',required=True, widget=forms.EmailInput(
        attrs={'class':"form-control", 'placeholder': "Email"}))
    edad = forms.IntegerField(label='Edad',required=True, widget=forms.NumberInput(
        attrs={'class':"form-control", 'placeholder': "Edad"}))
    dni = forms.IntegerField(label='DNI',required=True, widget=forms.NumberInput(
        attrs={'class':"form-control", 'placeholder': "DNI"}))
    telefono = forms.CharField(label='Telefono',required=True, widget=forms.TextInput(
        attrs={'class':"form-control", 'placeholder': "Telefono"}))
    direccion = forms.CharField(label='Direccion',required=True, widget=forms.TextInput(
        attrs={'class':"form-control", 'placeholder': "Direccion"}))
    #fecha_consulta = forms.ChoiceField(choices= fecha, label='Fecha de Consulta', required=True, widget= forms.)
    #hora_consulta = forms.TimeField(label='Hora Consulta', widget=forms.)
    fecha_consulta = forms.DateField(label= 'Fecha Consulta', widget=forms.SelectDateWidget(years = range(2020,2021),
        attrs={'class':"form-control", 'placeholder': "Fecha Consulta"}))


    
    class Meta:

        model = Turno
        fields = ['nombre', 'obra_social', 'email','edad','dni','telefono', 'direccion']





