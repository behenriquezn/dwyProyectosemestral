from django.shortcuts import render, redirect
from .models import  Producto, Tienda
from django.db.models import Sum, Count
from django.contrib.auth.models import User
from django.contrib import messages
import requests

from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, HttpResponseBadRequest
from django.core import serializers
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required, permission_required
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

    dispo = FCMDevice()
    dispo.registration_id = token
    dispo.active = True

    if request.user.is_authenticated:
        dispo.user =  request.user
    
    try:
        dispo.save()
        return HttpRequest(json.dumps({'mensaje','token guardado'}))
    except:
        return HttpResponseBadRequest(json.dumps({'mensaje':'no se pudo almacenar el token'}))


# Create your views here.

def index(request):
    return render(request, 'core/index.html')

@login_required(login_url='/login/')
def agregarTienda(request):
    if request.POST:
        nombre = request.POST.get("nombreTienda")
        nombresucursal = request.POST.get("nombreSucursal")
        direccion  = request.POST.get("Direccion")
        ciudad  = request.POST.get("Ciudad")
        region  = request.POST.get("Region")
    
        '''tienda = Tienda(
            nombre=nombre,
            nombresucursal=nombresucursal,
            direccion=direccion,
            ciudad=ciudad
            region=region
        )

        tienda.save()'''

        datos_tienda = {
            "nombre":nombre,
            "nombresucursal":nombresucursal,
            "direccion":direccion,
            "ciudad":ciudad,
            "region":region
        }


        resultado = requests.post("http://localhost:8000/api/tienda/", data=datos_tienda)
        return render(request,'core/agregarTienda.html',{'msg':'Tienda Agregada'})
    return render(request,'core/agregarTienda.html')

@login_required(login_url='/login/')
def agregarProductos(request):
    if request.POST:
        nombre = request.POST.get("nombreproducto")
        valor = request.POST.get("valorproducto")
        notas = request.POST.get("notas")
        valorpresupuestado = request.POST.get("valorPresupuestado")
        tiendanombre = request.POST.get("tiendanombre")
        numeroIdentificador = request.POST.get("nlistaproducto")
    
        '''producto = Productos(
            nombre=nombre,
            valor=valor,
            valorpresupuestado=valorpresupuestado,
            notas=notas
            tiendanombre=tiendanombre
            numeroIdentificador=numeroIdentificador
        )

        productos.save()'''

        datos_producto = {
            "nombre":nombre,
            "valor":valor,
            "valorpresupuestado":valorpresupuestado,
            "notas":notas,
            "tiendanombre":tiendanombre,
            "numeroIdentificador":numeroIdentificador
        }


        resultado = requests.post("http://localhost:8000/api/producto/", data=datos_producto)


        return render(request,'core/agregarProducto.html',{'msg':'Producto Agregado'})
    return render(request,'core/agregarProducto.html')

@login_required(login_url='/login/')
def modificar(request):
    if request.POST:
        nombre = request.POST.get("nombreProducto")
        valor = request.POST.get("valorProducto")

        try:
            producto = Producto.objects.get(nombre=nombre)
            producto.valor = valor
            producto.save()
            msg='Producto Modificado'
        except:
            msg='Producto NO Modificado'
    producto = Producto.objects.all()
    valortotal = Producto.objects.aggregate(Sum('valor'))['valor__sum']
    cantotal = Producto.objects.all().aggregate(Count('valor'))['valor__count']
    valorPtotal = Producto.objects.aggregate(Sum('valorpresupuestado'))['valorpresupuestado__sum']
    return render(request,'core/listaCompras.html',{'producto':producto,'msg':msg, 'valortotal':valortotal, 'cantotal':cantotal, 'valorPtotal':valorPtotal})    


@login_required(login_url='/login/')
def modificar_vista(request,id):
    try:
        producto = Producto.objects.get(nombre=id)
        return render(request,'core/agregarProducto_mod.html',{'producto':producto})
    except:
        msg = "No Existe Producto"
    producto = Producto.objects.all()
    return render(request,'core/listaCompras.html',{'producto':producto,'msg':msg})



@login_required(login_url='/login/')
def listaCompras(request):

    response = requests.get("http://localhost:8000/api/producto/")
    producto = response.json()
    valortotal = Producto.objects.aggregate(Sum('valor'))['valor__sum']
    cantotal = Producto.objects.all().aggregate(Count('valor'))['valor__count']
    valorPtotal = Producto.objects.aggregate(Sum('valorpresupuestado'))['valorpresupuestado__sum']
    if valortotal>valorPtotal:
            dispo = FCMDevice.objects.filter(active=True)
            dispo.send_message(
                title='Alerta de Presupuesto',
                body='Se a sobrepasado de su presupuesto',
                icon='/static/core/img/logo.png'
            )
    return render(request,'core/listaCompras.html',{'producto':producto, 'valortotal':valortotal, 'cantotal':cantotal, 'valorPtotal':valorPtotal})

@login_required(login_url='/login/')
def eliminar(request,id):
    try:
        producto = Producto.objects.get(nombre=id)
        producto.delete()
        msg ="Producto Eliminado"
    except:
        msg="No Elimino el Producto"
    producto = Producto.objects.all()
    valortotal = Producto.objects.aggregate(Sum('valor'))['valor__sum']
    cantotal = Producto.objects.all().aggregate(Count('valor'))['valor__count']
    valorPtotal = Producto.objects.aggregate(Sum('valorpresupuestado'))['valorpresupuestado__sum']
    if valortotal>valorPtotal:
            dispo = FCMDevice.objects.filter(active=True)
            dispo.send_message(
                title='Alerta de Presupuesto',
                body='Se ha sobrepasado de su presupuesto',
                icon='/static/img/logo.png'
            )
    return render(request,'core/listaCompras.html',{'producto':producto,'msg':msg, 'valortotal':valortotal, 'cantotal':cantotal, 'valorPtotal':valorPtotal})

def completarlista(request):
    
    msg ="Lista Completada"
    producto = Producto.objects.all()
    valortotal = Producto.objects.aggregate(Sum('valor'))['valor__sum']
    cantotal = Producto.objects.all().aggregate(Count('valor'))['valor__count']
    valorPtotal = Producto.objects.aggregate(Sum('valorpresupuestado'))['valorpresupuestado__sum']    
    dispo = FCMDevice.objects.filter(active=True)
    dispo.send_message(
        title='Compra completada',
        body='Se ha completado su lista de compras',
        icon='/static/core/img/logo.png'
    )
    return render(request,'core/listaCompras.html',{'producto':producto,'msg':msg, 'valortotal':valortotal, 'cantotal':cantotal, 'valorPtotal':valorPtotal}) 


def registro(request):
    if request.POST:
        nombre = request.POST.get("txtNombre")
        apellido = request.POST.get("txtApellido")
        email = request.POST.get("txtEmail")
        usuario = request.POST.get("txtUsuario")
        password1 = request.POST.get("txtPassword1")
        password2 = request.POST.get("txtPassword2")
        if password1!=password2:
            return render(request,'core/registro.html', {'msg':'Contraseñas incorrectas'})
        try:
            user = User.objects.get(username=usuario)
            return render(request,'core/registro.html', {'msg':'Usuario ya existe'})
        except:
            try:
                user = User.objects.get(email=email)
                return render(request,'core/registro.html', {'msg':'Email ya existe'})
            except:
                user = User()
                user.username = usuario
                user.first_name = nombre
                user.last_name = apellido
                user.email = email
                user.set_password(password1)
                user.save()

                user = authenticate(request, username=usuario, password=password1)
                return render(request,'core/registro.html', {'msg':'Usuario registrado exitosamente'})
    return render(request, 'core/registro.html')



def logout_sesion(request):
    logout(request)
    return render(request, 'core/index.html')


def ingresar(request):
    if request.POST:
        usuario = request.POST.get("Usuario")
        clave = request.POST.get("Pass")
        us = authenticate(request, username=usuario,password=clave)
        if us is not None:
            login(request, us)
           
            return render(request,'core/index.html')
        else:
            return render(request,'core/login.html',{'msg':'Usuario/Contraseña incorrectos.'})
    return render(request,'core/login.html')

def listar_por_nlista(request): 
    numeroIdentificador = request.POST.get("txtnumeroIdentificador")
    if numeroIdentificador is '':
        producto = Producto.objects.all()
        valortotal = Producto.objects.aggregate(Sum('valor'))['valor__sum']
        cantotal = Producto.objects.all().aggregate(Count('valor'))['valor__count']
        valorPtotal = Producto.objects.aggregate(Sum('valorpresupuestado'))['valorpresupuestado__sum']
    else:
        producto = Producto.objects.filter(numeroIdentificador=numeroIdentificador)
        valortotal = Producto.objects.aggregate(Sum('valor'))['valor__sum']
        cantotal = Producto.objects.all().aggregate(Count('valor'))['valor__count']
        valorPtotal = Producto.objects.aggregate(Sum('valorpresupuestado'))['valorpresupuestado__sum']

    return render(request,'core/listaCompras.html',{'producto':producto, 'valortotal':valortotal, 'cantotal':cantotal, 'valorPtotal':valorPtotal})        
