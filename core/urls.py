from django.urls import path
from .views import index, formulario, formularioInsumo, galeria, registro, quienesSomos, ubicacion, agregarEmpleado, agregarInsumo, modificarEmpleado, modificarInsumo, eliminarEmpleado, eliminarInsumo, contactoFinal,listar_por_nombre_api,listar_por_precio_api,guardar_token
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls import include

urlpatterns = [
    path('', index, name="index"),
    path('formulario/', formulario, name="formulario"),
    path('formularioInsumo/', formularioInsumo, name="formularioInsumo"),
    path('galeria/', galeria, name="galeria"),
    path('registro/', registro, name="registro"),
    path('quienesSomos/', quienesSomos, name="quienesSomos"),
    path('ubicacion/', ubicacion, name="ubicacion"),
    path('agregarEmpleado/', agregarEmpleado, name="agregarEmpleado"),
    path('agregarInsumo/', agregarInsumo, name="agregarInsumo"),
    path('modificarEmpleado/<id>', modificarEmpleado, name="modificarEmpleado"),
    path('modificarInsumo/<id>', modificarInsumo, name="modificarInsumo"),
    path('eliminarEmpleado/<id>',eliminarEmpleado, name="eliminarEmpleado"),
    path('eliminarInsumo/<id>',eliminarInsumo, name="eliminarInsumo"),
    path('login/', LoginView.as_view(template_name="core/login.html"), name="login"),
    path('logout/', LogoutView.as_view(template_name="core/logout.html"), name="logout"),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('contactoFinal/', contactoFinal, name="contactoFinal"),
    path("lista_nombre/",listar_por_nombre_api,name="LISTANOMBRE"),
    path("lista_precio/",listar_por_precio_api,name='LISTAPRECIO'),
    path("guardar-token/",guardar_token,name='guardar-token'),
]

