from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from hotel.models import Hotel 
from django.db.models import Q
 


class Vregistro(View):
    def get(self, request):
        print("hizo get")
        form = UserCreationForm()
        return render(request, "nuevoregistro.html", {"form": form})

    def post(self, request):
        print("hizo post")
        global usuario
        form = UserCreationForm(request.POST)
        print("hice post")
        if form.is_valid():
            print("entre al if")
            usuario = form.save()
            login(request, usuario)
            return redirect("/")
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, "nuevoregistro.html", {"form": form})


def autenticar(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_user = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            global usuario
            usuario = authenticate(username=nombre_user, password=contra)
            if usuario is not None:
                login(request, usuario)
                return redirect("/")
            else:
                messages.error(request, "usaurio no valido")
        else:
            messages.error(request, "informacion incorrecta")

    form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def cerrar_sesion(request):
    logout(request)
    return redirect("/")


def home(request):
    return render(request, "index.html")




def acerca(request):
    return render(request, "about.html")


def registro(request):
    return render(request, "nuevoregistro.html")


def buscar(request):
    
    nombre=request.GET.get('nombre')
    estrella=request.GET.get('estrella')
    capacidad=request.GET.get('capacidad')
    precio=request.GET.get('precio')
    estado=request.GET.get('estado')
   
    
    if (estado=='activo'):
        estado=1 
    else:
        estado=0 
     
    
    hoteles=Hotel.objects.filter(
         Q(nombre__icontains = nombre)&
         Q(estrellas__icontains = estrella)&
         Q(capacidad__icontains = capacidad)& 
         Q(precio__icontains = precio)&
         Q(estado__icontains = estado)
        
        
        
         
        ).distinct()
    return render(request, "hoteles.html", {'hotel': hoteles})