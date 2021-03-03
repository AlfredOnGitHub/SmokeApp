from django.db import models
from django.utils import timezone

class Registro(models.Model): 
    Meses = [("EN","Enero"),
            ("FE","Febrero"),
            ("MA","Marzo"),
            ("AB","Abril"),]
    Cantidad = models.DecimalField(max_digits=5,decimal_places=2)
    Inversión = models.DecimalField(max_digits=5,decimal_places=2)
    Fecha = models.DateField(default=timezone.now)
    Mes = models.CharField(max_length=2, choices=Meses, default="EN",)


    def registrar(self):
        self.save()

    def __str__(self):
        return str(self.Fecha)