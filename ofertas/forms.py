from django import forms
from .models import Oferta, Ofertadatos


#formulario

class ofertaform(forms.ModelForm):
    

    class Meta:
        model=Oferta
        fields=[
            "nombre",
            "precio",
            "capacidad",
            "estado",
            "hotel",

        ]
        widgets={
            "nombre": forms.TextInput(attrs={"class": "form-input", "id":"nombre","Placeholder": "nombre"}),
            "precio": forms.TextInput(attrs={"class": "form-input","Placeholder": "apellidos", "id":"precio"}),
            "capacidad": forms.TextInput(attrs={"class": "form-input","Placeholder": "correo", "id":"capacidad"}),
            "estado": forms.TextInput(attrs={"class": "form-input","Placeholder": "CI", "id":"estado"}),
            "hotel": forms.TextInput(attrs={"class": "form-input","Placeholder": "pais", "id":"hotel"}),
        }
        
class ofertadatosform(forms.ModelForm):
    
    class Meta:
        model=Ofertadatos
        fields=[
            "nombre",
            "apellidos",
            "correo",
            "ci",
            "pais",
            "fecha_entrada",
            "fecha_salida",
            "codigo",

        ]
        widgets={
            "nombre": forms.TextInput(attrs={"class": "form-input", "id":"nombre","Placeholder": "Nombre"}),
            "apellidos": forms.TextInput(attrs={"class": "form-input","Placeholder": "apellidos", "id":"apellido"}),
            "correo": forms.TextInput(attrs={"class": "form-input","Placeholder": "correo", "id":"correo"}),
            "ci": forms.TextInput(attrs={"class": "form-input","Placeholder": "CI", "id":"ci"}),
            "pais": forms.TextInput(attrs={"class": "form-input","Placeholder": "pais", "id":"pais"}),
            "fecha_entrada": forms.TextInput(attrs={"class": "form-input","Placeholder": "dia/mes", "id":"fe"}),
            "fecha_salida": forms.TextInput(attrs={"class": "form-input","Placeholder": "dia/mes", "id":"fs"}),
            "codigo": forms.TextInput(attrs={"class": "form-input","Placeholder": "", "id":"codigo"}),
           
        }        