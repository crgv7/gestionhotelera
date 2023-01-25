from django.contrib import admin
from .models import Oferta

# Register your models here.

class OfertasAdmin(admin.ModelAdmin):
    list_display=("nombre","capacidad","precio", "hotel", "estado")

admin.site.register(Oferta,OfertasAdmin)