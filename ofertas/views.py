from django.shortcuts import render, redirect
from .models import Oferta, Ofertadatos
from hotel.models import Hotel
from .forms import ofertaform, ofertadatosform
from django.contrib.auth.decorators import login_required
import random
from django.db.models import Q

@login_required
def ofertas(request):
    oferta=Oferta.objects.all()
    return render(request, "ofertas.html", {"oferta": oferta})

# Create your views here.
@login_required
def panel(request):
    
    ofertas=Ofertadatos.objects.all().filter(user=request.user) # hace una consulta y hacer filtro por el nombre de usuario
    
    #hotel=Hotel.objects.all().filter(id=ofertas.hotel_id)                                                               # selecciona todos los objetos de la tabla que coincida con el nombre del usuario y lo guarda
                                                                   # en esa variable
    buscar=request.POST.get('buscar')
    
  
    if buscar:
        ofertas=Oferta.objects.filter(
         Q(nombre__icontains = buscar)| 
         Q(capacidad__icontains = buscar)|
         Q(precio__icontains = buscar) 
        
        ).distinct()
        
    return render(request, "panel_oferta.html", {"oferta": ofertas
                                                 }) # carga el html
@login_required
def add_oferta(request, id):
        context={}   
        ofert=Oferta.objects.get(id=id)
        hotel=Hotel.objects.get(id=ofert.hotel_id)
        print(hotel.nombre)
       
# si no es post muestra el formulario
        form=ofertaform(initial={'hotel': hotel.nombre,
                                  'nombre': ofert.nombre,
                                      'capacidad':ofert.capacidad,
                                          'precio': ofert.precio,
                                          'estado':ofert.estado
                                 
                                 })#El nombre de usurio ya inicalizado en el campo
        
        #desabilita el campo
        form.fields['hotel'].disabled = "True"
        form.fields['nombre'].disabled = "True"
        form.fields['capacidad'].disabled = "True"
        form.fields['precio'].disabled = "True"
        form.fields['estado'].disabled="True"
        context["form"]=form
        
         #form ofertadatos:
         
        formr=ofertadatosform
        
        if request.method == "POST": # si el metod es post realiza la condicion
            formr=ofertadatosform(request.POST, initial={ 'codigo': random.randint(1, 10000) ,                                                
                                                                                                               })
             #habilita el campo para que pase el dato atraves  del post,
            formr.fields['codigo'].disabled = "False"
            formr.user=request.user
            formr.hotel_id=ofert.hotel_id
            formr.oferta_id=ofert.id
            formr.hotel=ofert.hotel_id
            
            if formr.is_valid():
                print("es valido")
                                       # validacion del formula
                nombre=formr.cleaned_data.get("nombre")
                apellidos=formr.cleaned_data.get("apellidos")
                correo=formr.cleaned_data.get("correo")
                ci=formr.cleaned_data.get("ci")
                fecha_entrada=formr.cleaned_data.get("fecha_entrada")
                fecha_salida=formr.cleaned_data.get("fecha_salida")
                pais=formr.cleaned_data.get("pais")
                codigo=formr.cleaned_data.get("codigo")
                hotel=formr.cleaned_data.get("hotel")
               
                reg=Ofertadatos.objects.create( #crea objetos en la tabla
                    nombre=nombre,
                    apellidos=apellidos,
                    correo=correo,
                    ci=ci,
                    fecha_entrada=fecha_entrada,
                    fecha_salida=fecha_salida,
                    pais=pais,
                    codigo=codigo,
                    hotel_id=ofert.hotel_id,
                    oferta_id=ofert.id,
                    user=request.user
                )
                reg.save()
                
                
        formr=ofertadatosform(initial={ 
                                       'codigo': random.randint(1, 10000) } )
        formr.fields['codigo'].disabled = "True" 
             
        
        return render(request, "add_ofertas.html",{"form": form,
                                                    "formr":formr})


def eliminar(request, id): # eliminar obejeto
    #funcion por implemntar
    ofertadatos=Ofertadatos.objects.all().filter(user=request.user)
    ofertadatos=Ofertadatos.objects.get(id=id)
    ofertadatos.delete()
    return redirect("/ofertas/panel/")
   




@login_required
def editar(request, id): # editar reservacion

    
    ofertadatos=Ofertadatos.objects.get(id=id)


    formr=ofertadatosform(initial={'nombre':ofertadatos.nombre,
                                  'apellidos': ofertadatos.apellidos,
                                  'correo': ofertadatos.correo,
                                  'ci': ofertadatos.ci,
                                  'fecha_entrada': ofertadatos.fecha_entrada,
                                  'fecha_salida': ofertadatos.fecha_salida,
                                  'pais': ofertadatos.pais,
                                  'codigo':ofertadatos.codigo,
                                 
                                
                                  })
  
     #desabilita el campo
    formr.fields['codigo'].disabled = "True"
  
    form=ofertaform(initial={'nombre':ofertadatos.oferta.nombre,
                                  'capacidad': ofertadatos.oferta.capacidad,
                                  'precio': ofertadatos.oferta.precio,
                                  'estado': ofertadatos.oferta.estado,
                                  'hotel': ofertadatos.oferta.hotel
                                
                                  })
  
     #desabilita el campo
    form.fields['hotel'].disabled = "True"
    form.fields['nombre'].disabled = "True"
    form.fields['capacidad'].disabled = "True"
    form.fields['precio'].disabled = "True"
    form.fields['estado'].disabled="True"
    
    
    if request.method == "POST":
         
        formr=ofertadatosform(request.POST, initial={           'codigo': random.randint(1, 10000)
                                                     })

        #habilita el campo para que pase el dato atraves  del post,
        formr.fields['codigo'].disabled = "False"
        formr.user=request.user
    
        
        
        if formr.is_valid():                                  # validacion del formula
            nombre=formr.cleaned_data.get("nombre")
            apellidos=formr.cleaned_data.get("apellidos")
            correo=formr.cleaned_data.get("correo")
            ci=formr.cleaned_data.get("ci")
            fecha_entrada=formr.cleaned_data.get("fecha_entrada")
            fecha_salida=formr.cleaned_data.get("fecha_salida")
            pais=formr.cleaned_data.get("pais")
            codigo=formr.cleaned_data.get("codigo")
          
      

            ofertadatos.nombre=nombre
            ofertadatos.apellidos=apellidos
            ofertadatos.correo=correo
            ofertadatos.ci=ci
            ofertadatos.fecha_entrada=fecha_entrada
            ofertadatos.fecha_salida=fecha_salida
            ofertadatos.codigo=codigo
          
            

            ofertadatos.save()
        
    # ofertadatos    
     

    return render(request, "editar_oferta.html", {"form": form,
                                                  "formr":formr})