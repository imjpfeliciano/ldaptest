#enconding:utf-8
from altas.models import Alumno
from altas.forms import AlumnoForm, ContactoForm, ContrasenaForm
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMessage
from django.template import RequestContext

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Greeting

# Create your views here.
def index(request):
    return HttpResponse('Hello from Python!')

def test(request):
    return HttpResponse('testing')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

def inicio(request):
    return render_to_response('inicio.html', context_instance=RequestContext(request))

def registro(request):
    if request.method == 'POST':
        formulario = AlumnoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = AlumnoForm()
    return render_to_response('registro.html', {'formulario':formulario}, context_instance=RequestContext(request))

def generar_script(request):
    usuarios = Alumno.objects.all()
    return render_to_response('script.html', {'datos':usuarios.order_by('matricula')}, context_instance=RequestContext(request))

def contacto(request):
    if request.method == 'POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            titulo = 'Mensaje desde la aplicacion de Registro LDAP'
            contenido = formulario.cleaned_data['mensaje'] + "\n"
            contenido += 'Comunicarse a: ' + formulario.cleaned_data['correo']
            correo = EmailMessage(titulo, contenido, to=['electronica.unicaribe@gmail.com'])
            correo.send()
            return HttpResponseRedirect('/')
    else:
        formulario = ContactoForm()
    return render_to_response('contactoform.html', {'formulario':formulario}, context_instance=RequestContext(request))

def contrasena(request):
    if request.method == 'POST':
        formulario = ContrasenaForm(request.POST)
        if formulario.is_valid():
            usuario = Alumno.objects.get(matricula__exact=formulario.cleaned_data['matricula'])
            titulo = 'Solicitud de contrasena - LDAP Telematica'
            contenido = 'Hola ' + usuario.nombre + '\n'
            contenido += 'su contrasena es: ' + usuario.contrasena
            correo = EmailMessage(titulo, contenido, to=[formulario.cleaned_data['matricula'] + '@ucaribe.edu.mx'])
            correo.send()
            return HttpResponseRedirect('/')
    else:
        formulario = ContrasenaForm()
    return render_to_response('contrasenaform.html', {'formulario':formulario}, context_instance=RequestContext(request))



