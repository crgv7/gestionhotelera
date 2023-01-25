from django.db import models

# Create your models here.
class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=100, blank=False, null=False)
    capacidad = models.IntegerField('Capacidad del Hotel', blank=False, null=False)
    precio = models.IntegerField('Precio', blank=False, null=False)
    estrellas = models.IntegerField('Estrellas')
    estado = models.BooleanField('Activo/No Activo', default=True)
    imagen=models.ImageField()
    class Meta:
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hoteles'

    def __str__(self):
        return self.nombre
    
