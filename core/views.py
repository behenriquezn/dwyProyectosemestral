from django.shortcuts import render, redirect
from .models import Empleado, Insumo, ContactoFinal
from django.contrib.auth.models import User
from .forms import EmpleadoForm, InsumoForm, UserRegisterForm, ContactoFinalForm
from django.contrib import messages
import requests

from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, HttpResponseBadRequest
from django.core import serializers
import json
from fcm_django.models import FCMDevice

@csrf_exempt
@require_http_methods(['POST'])
def guardar_token(request):
    body = request.body.decode('utf-8')
    bodyDatos = json.loads(body)
    token = bodyDatos['token']

    existe =  FCMDevice.objects.filter(registration_id=token,active=True)
    if len(existe)>0:
        return HttpResponseBadRequest(json.dumps({'mensaje','token ya existe'}))

    dispositivo = FCMDevice()
    dispositivo.registration_id = token
    dispositivo.active = True

    if request.user.is_authenticated:
        dispositivo.user =  request.user
    
    try:
        dispositivo.save()
        return HttpRequest(json.dumps({'mensaje','token guardado'}))
    except:
        return HttpResponseBadRequest(json.dumps({'mensaje':'no se pudo almacenar el token'}))



# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def formulario(request):
    empleadoAll = User.objects.all()
    datos = {
        'listaEmpleados' : empleadoAll
    }

    return render(request, 'core/formulario.html', datos)

def agregarEmpleado(request):
    datos = {
        'form' : EmpleadoForm()  

    }
    if request.method == 'POST':
        formu = EmpleadoForm(request.POST)
        if formu.is_valid():
            formu.save()
            datos['mensaje'] = "Empleado Guardado Correctamente"

    return render(request, 'core/agregarEmpleado.html', datos)

def modificarEmpleado(request, id):
    usuario = User.objects.get(id=id)
    datos = {
        'form' : UserRegisterForm(instance=usuario)
    }
    if request.method == 'POST':
        formu = UserRegisterForm(data=request.POST, instance=usuario)
        if formu.is_valid():
            formu.save()
            datos['mensaje'] = "El Usuario ah Modificado Correctamente"
            datos['form'] = formu

    return render(request, 'core/modificarEmpleado.html', datos)

def contactoFinal(request):
    datos = {
        'form' : ContactoFinalForm()

    }
    if request.method == 'POST':
        formuCon = ContactoFinalForm(request.POST)
        if formuCon.is_valid():
            formuCon.save()
            datos['mensaje'] = "Cliente Guardado Correctamente"
#
#        datos_contacto = {
#           "nombre":nombre,
#            "apellido":apellido,
#            "asunto":asunto,
#            "tipoCon":tipoCon,
#            "mensaje":mensaje
#        }
#        resultado = requests.post("http://localhost:8000/api/contactoFinal/", data=datos_contacto)
#        #notificacion
#        admins = FCMDevice.objects.filter(active=True)
#        admins.send_message(
#            title='Nuevo Contacto',
#            body='Se ha recibido un nuevo contacto, Asunto: '+asunto,
#            icon='/static/img/logo1.png'
#        )
     
    return render(request, 'core/modificarEmpleado.html', datos)

def eliminarEmpleado(request, id):
    usuario = User.objects.get(id=id)
    usuario.delete()

    return redirect(to="formulario")



def formularioInsumo(request):
    insumosAll = Insumo.objects.all()
    response = requests.get("http://localhost:8000/api/insumo/")
    insumo = response.json()
    return render(request, 'core/formularioInsumo.html',{'listaInsumos':insumosAll})



def agregarInsumo(request):
    datos = {
        'form' : InsumoForm()  

    }
    if request.method == 'POST':
        formuIn = InsumoForm(request.POST)
        if formuIn.is_valid():
            formuIn.save()
            datos['mensaje'] = "Insumo Guardado Correctamente"

        FCMDevice.send_message(
            title='Nuevo insumo',
            body='Se ha agregado un nuevo insumo: ',
            icon='/static/img/logo1.png'
        )


    return render(request, 'core/agregarInsumo.html', datos)

def modificarInsumo(request, id):
    insumo = Insumo.objects.get(id=id)
    datos = {
        'form' : InsumoForm(instance=insumo)
    }
    if request.method == 'POST':
        formuIn = InsumoForm(data=request.POST, instance=Insumo)
        if formuIn.is_valid():
            formuIn.save()
            datos['mensaje'] = "Insumo Modificado Correctamente"
            datos['form'] = formuIn

    return render(request, 'core/modificarInsumos.html', datos)

def eliminarInsumo(request, id):
    insumo = Insumo.objects.get(id=id)
    insumo.delete()

    return redirect(to="formularioInsumo")

def galeria(request):
    return render(request, 'core/galeria.html')

def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect ('index')

    else:
        form = UserRegisterForm()

    context = {'form' : form}
    return render(request, 'core/registro.html', context)

def quienesSomos(request):
    return render(request, 'core/quienesSomos.html')

def ubicacion(request):
    return render(request, 'core/ubicacion.html')


def listar_por_nombre_api(request):
    InsumoForm.Meta.model.nombre = request.POST.get("txtNombre")
    response = requests.get("http://localhost:8000/api/insumo_nombre/"+InsumoForm.Meta.model.nombre+"/")
    insumo = response.json()
    return render(request,'core/formularioInsumo.html',{'insumo':insumo})

def listar_por_precio_api(request):
    InsumoForm.Meta.model.precio = request.POST.get("txtPrecio")
    response = requests.get("http://localhost:8000/api/insumo_precio/"+InsumoForm.Meta.model.precio+"/")
    insumo = response.json()
    return render(request,'core/formularioInsumo.html',{'insumo':insumo})