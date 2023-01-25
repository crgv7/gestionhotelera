from django import forms
from .models import Reservacion


#formulario

class reservacionform(forms.ModelForm):
    

    class Meta:
        model=Reservacion
        fields=[
            "nombre",
            "apellidos",
            "correo",
            "ci",
            "pais",
            "hotel",
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
            "hotel": forms.TextInput(attrs={"class": "form-input","Placeholder": "", "id":"hotel"}),
        }