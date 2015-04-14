#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField, PasswordInput

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

CARRERAS = ((u'Telematica', 'Telemática'),
            (u'Industrial', 'Industrial'),
            (u'Logistica', 'Logistica'),
            (u'Ambiental', 'Ambiental'),)

class Alumno(models.Model):
    matricula = models.CharField(max_length=9, unique=True, default='')
    contrasena = models.CharField(max_length=16, verbose_name='Contraseña', default='')

    mail = models.CharField(max_length=30, verbose_name='Correo Electronico', default='example@ucaribe.edu.mx')
    nombre = models.CharField(max_length=15, default='')
    ap_paterno = models.CharField(max_length=12, verbose_name='Apellido Paterno', default='')
    ap_materno = models.CharField(max_length=12, verbose_name='Apellido Materno', default='')

    nombre_corto = models.CharField(max_length=15, verbose_name='Nickname', default='')
    carrera = models.CharField(choices=CARRERAS, max_length=10)

    def __unicode__(self):
        return self.matricula

class Contacto(models.Model):
    correo = models.EmailField(max_length=75, verbose_name='Ingresa tu Matricula')
    mensaje = models.CharField(max_length=200, verbose_name='Deja tu Comentario')

    def __unicode__(self):
        return self.correo