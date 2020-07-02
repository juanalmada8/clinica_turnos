from django import forms


class TurnosForm(forms.Form):

    nombre = forms.CharField(label='Nombre',required=True)
    apellido = forms.CharField(label='Apellido',required=True)
    obra_social = forms.CharField(label='Obra Social',required=True)
    email = forms.EmailField(label='Email',required=True)
    edad = forms.IntegerField(label='Edad',required=True)
    dni = forms.IntegerField(label='DNI',required=True)
    telefono = forms.CharField(label='Telefono',required=True)
    direccion = forms.CharField(label='Direccion',required=True)





