from django.shortcuts import render
from django.utils import timezone
from .models import Registro

def recuento(request):
    cuentas = Registro.objects.filter(Fecha__lte=timezone.now()).order_by('-Fecha')
    return render(request, 'FinanzasApp/general.html', {'cuentas':cuentas})
