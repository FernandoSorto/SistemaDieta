from django.db import models

# Create your models here.

class Ingrediente(models.Model):
    nomIngrediente = models.CharField(max_length=200, blank= False, null=False, default='')
    tipo = models.CharField(max_length=60, blank=False, null=False)
    cantidad = models.CharField(max_length=70, blank=False, null=False)

    def __str__(self):
        return self.nomIngrediente + ", Cantidad: " + self.cantidad

class Plato(models.Model):
    Snack = 'Snack'
    Desayuno = 'Desayuno'
    Almuerzo = 'Almuerzo'
    Cena = 'Cena'
    platoChoices = (
        (Snack, 'Snack'),
        (Desayuno, 'Desayuno'),
        (Almuerzo, 'Almuerzo'),
        (Cena, 'Cena')
    )
    alta = 'Alta'
    baja = 'Baja'
    azSalChoices = (
        (alta, 'Alta'),
        (baja, 'Baja')
    )
    nombre = models.CharField(max_length=60, blank=False, null=False)
    preparacion = models.CharField(max_length=600, blank=False, null=False)
    tiempoComida = models.CharField(max_length=15, choices=platoChoices, default=None, blank=False, null=False)
    tipoDieta = models.CharField(max_length=30, default=None, blank=False, null=False)
    dietaCal = models.CharField(max_length=100, default=None, blank=False, null=False)
    azucar = models.CharField(max_length=15, choices=azSalChoices, default=None, blank=False, null=False)
    sal = models.CharField(max_length=15, choices=azSalChoices, default=None, blank=False, null=False)
    ingredientes = models.ManyToManyField(Ingrediente)
