from django.contrib import admin
from django.conf.urls import include
from django.conf.urls import url
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^api/producto/$', views.ProductoViewSet.as_view()),
    url(r'^api/tienda/$', views.TiendaViewSet.as_view()),
    url(r'^api/producto_lista/(?P<numeroIdentificador>[0-9].+)/$',views.ProductoFiltroListaViewSet.as_view()),
]

urlpatterns=format_suffix_patterns(urlpatterns)
