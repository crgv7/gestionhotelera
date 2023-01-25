from django.contrib import admin
from .models import Hotel

# Register your models here.

class Hoteladmin(admin.ModelAdmin):
    list_display=("nombre","capacidad","precio", "estrellas", "estado")


admin.site.register(Hotel, Hoteladmin)