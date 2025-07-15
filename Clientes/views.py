from django.shortcuts import render
from Servicios.models import Servicios

def home_view(request):
    return render(request, "clientes/homeCliente.html")


def servicios_view(request):
    servicios = Servicios.objects.all()
    return render(request, 'servicios.html', {'servicios': servicios})
