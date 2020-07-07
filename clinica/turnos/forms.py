from django import forms
from .models import Turno



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
    
    class Meta:
        model = Turno
        fields = ['nombre', 'obra_social', 'email','edad','dni','telefono', 'direccion']





