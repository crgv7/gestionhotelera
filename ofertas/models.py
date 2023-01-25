from django.db import models
from django.contrib.auth.models import User
from hotel.models import Hotel



# Create your models here.
class Oferta(models.Model):
    precio = models.IntegerField('Precio', blank=False, null=False)
    capacidad = models.IntegerField('Cantidad de Personas', blank=False, null=False)
    nombre = models.CharField('Nombre', max_length=100, blank=False, null=False)
   #hotel = models.CharField('Hotel', max_length=100, blank=False, null=False)
    estado= models.BooleanField('Activa/No Activa',default=False)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  

    


    class Meta:
        verbose_name = 'Oferta'
        verbose_name_plural = 'Ofertas'

    def __str__(self):
        return self.nombre
    
class Ofertadatos(models.Model):
    nombre = models.CharField('Nombre', max_length=100, blank=False, null=False)
    apellidos = models.CharField('Apellidos', max_length=100, blank=False, null=False)
    correo = models.EmailField('Email', blank=False, null=False)
    pais = models.CharField('País', max_length=100, blank=False, null=False)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    ci = models.CharField('Carnet de Identidad', max_length=11, blank=False, null=False)
    fecha_entrada = models.CharField('Fecha de Entrada', max_length=100,blank=False, null=False)
    fecha_salida = models.CharField('Fecha de Salida', max_length=100, blank=False, null=False)
    codigo = models.IntegerField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    oferta=models.ForeignKey(Oferta, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Reservación'
        verbose_name_plural = 'Reservaciones'

    def __str__(self):
        return self.nombre
    
  