from django.urls import path
from .views import index, registro, agregarProductos,ingresar,logout_sesion,completarlista ,listar_por_nlista,guardar_token,listaCompras,modificar ,modificar_vista,agregarTienda,eliminar
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls import include

urlpatterns = [
    path('', index, name="index"),
    path('registro/', registro, name="registro"),
    path('agregarProducto/', agregarProductos, name="agregarProducto"),
    
    path('agregarTienda/', agregarTienda, name="agregarTienda"),    
    path('listaCompras/', listaCompras, name="listaCompras"),
    path('modificar/', modificar, name="modificar"),
    path('modificar_vista/<id>/',modificar_vista,name='modificarVista'),
    path('login/', ingresar,name='login'),
    path('logout_sesion/',logout_sesion,name='logout'),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('eliminar/<id>/',eliminar,name='eliminar'),
    path('completarlista/',completarlista,name='completarlista'),
    path("guardar-token/",guardar_token,name='guardar-token'),
    path("listar_por_nlista/",listar_por_nlista,name="productoLista"),

]

