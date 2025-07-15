from django import forms
from Auth.models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'correo', 'telefono', 'direccion']

    def __str__(self):
        return self.nombre

