from django.shortcuts import render, redirect
from .models import Reservacion
from hotel.models import Hotel
from .forms import reservacionform
from django.contrib.auth.decorators import login_required
import random
from django.db.models import Q



# Create your views here.
@login_required
def panel(request):

    reservaciones=Reservacion.objects.all().filter(user=request.user) # hace una consulta y hacer filtro por el nombre de usuario
                                                                   # selecciona todos los objetos de la tabla que coincida con el nombre del usuario y lo guarda
                                                                   # en esa variable
    buscar=request.POST.get('buscar')
    
  
    if buscar:
        reservaciones=Reservacion.objects.filter(
         Q(nombre__icontains = buscar)| 
         Q(apellidos__icontains = buscar)|
         Q(pais__icontains = buscar) |
         Q(correo__icontains = buscar) 
        ).distinct()
        
    return render(request, "panel.html", {"reservaciones":reservaciones}) # carga el html
@login_required
def add_reservacion(request, id):
        context={}
        reserv=Hotel.objects.get(id=id)
        if request.method == "POST": # si el metod es post realiza la condicion
            form=reservacionform(request.POST, initial={'hotel': reserv.id,
                                                        'codigo': random.randint(1, 10000)

                                                        })

             #habilita el campo para que pase el dato atraves  del post,
            form.fields['codigo'].disabled = "False"
            form.fields['hotel'].disabled = "False"
            form.user=request.user
            
            if form.is_valid():
                print("es valido")
                                       # validacion del formula
                nombre=form.cleaned_data.get("nombre")
                apellidos=form.cleaned_data.get("apellidos")
                correo=form.cleaned_data.get("correo")
                ci=form.cleaned_data.get("ci")
                fecha_entrada=form.cleaned_data.get("fecha_entrada")
                fecha_salida=form.cleaned_data.get("fecha_salida")
                pais=form.cleaned_data.get("pais")
                codigo=form.cleaned_data.get("codigo")
                hotel=form.cleaned_data.get("hotel")



                reg=Reservacion.objects.create( #crea objetos en la tabla
                    nombre=nombre,
                    apellidos=apellidos,
                    correo=correo,
                    ci=ci,
                    fecha_entrada=fecha_entrada,
                    fecha_salida=fecha_salida,
                    pais=pais,
                    codigo=codigo,
                    hotel=hotel,
                    user=request.user
                )
                reg.save()
# si no es post muestra el formulario

        form=reservacionform(initial={'hotel': reserv.nombre,
                                      'codigo': random.randint(1, 10000)
                                      } )#El nombre de usurio ya inicalizado en el campo

        #desabilita el campo
        form.fields['codigo'].disabled = "True"
        form.fields['hotel'].disabled = "True"
        context["form"]=form
        return render(request, "add_reservacion.html", context)


def eliminar(request, id): # eliminar obejeto
    reservaciones=Reservacion.objects.all().filter(user=request.user)
    reserv=Reservacion.objects.get(id=id)
    reserv.delete()
    return redirect("/reservacion/panel/")

@login_required
def editar(request, id): # editar reservacion

    reserv=Reservacion.objects.get(id=id)


    context={}
    form=reservacionform(initial={'nombre':reserv.nombre,
                                  'apellidos': reserv.apellidos,
                                  'correo': reserv.correo,
                                  'ci': reserv.ci,
                                  'fecha_entrada': reserv.fecha_entrada,
                                  'fecha_salida': reserv.fecha_salida,
                                  'pais': reserv.pais,
                                  'codigo':reserv.codigo,
                                  'hotel':reserv.hotel_id
                                
                                  })
    context["form"]=form
     #desabilita el campo
    form.fields['codigo'].disabled = "True"
    form.fields['hotel'].disabled = "True"
    if request.method == "POST":
        
        hotelname=reserv.hotel_id
        name=Hotel.objects.get(id=hotelname)
        
        print(name)
        form=reservacionform(request.POST, initial={    'hotel':reserv.hotel_id,
                                                        'codigo': random.randint(1, 10000)

                                                        })

        #habilita el campo para que pase el dato atraves  del post,
        form.fields['codigo'].disabled = "False"
        form.fields['hotel'].disabled = "False"

        if form.is_valid():                                  # validacion del formula
            nombre=form.cleaned_data.get("nombre")
            apellidos=form.cleaned_data.get("apellidos")
            correo=form.cleaned_data.get("correo")
            ci=form.cleaned_data.get("ci")
            fecha_entrada=form.cleaned_data.get("fecha_entrada")
            fecha_salida=form.cleaned_data.get("fecha_salida")
            pais=form.cleaned_data.get("pais")
            codigo=form.cleaned_data.get("codigo")
            hotel=form.cleaned_data.get("hotel")
      

            reserv.nombre=nombre
            reserv.apellidos=apellidos
            reserv.correo=correo
            reserv.ci=ci
            reserv.fecha_entrada=fecha_entrada
            reserv.fecha_salida=fecha_salida
            reserv.pais=pais
            reserv.codigo=codigo
            reserv.hotel=hotel
            

            reserv.save()
            return redirect('/reservacion/panel/')

    return render(request, "editar_reservacion.html", context)