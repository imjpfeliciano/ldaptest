#encoding:utf-8
from django.forms import ModelForm
from django import forms
from altas.models import Alumno, CARRERAS, Contacto

class AlumnoForm(ModelForm):
    class Meta:
        model = Alumno
        widgets = {
            'contrasena': forms.PasswordInput()
        }

class ContactoForm(forms.Form):
    correo = forms.EmailField(label='Correo Electrónico')
    mensaje = forms.CharField(widget=forms.Textarea)

class ContrasenaForm(forms.Form):
    matricula = forms.CharField(label='Matricula')

    
