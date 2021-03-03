from django.shortcuts import render
from .models import grafico

def visual(request):
    return render(request, 'visualization/grafico.html', {'visual': visual})
