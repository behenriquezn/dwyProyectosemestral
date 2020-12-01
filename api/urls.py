from django.contrib import admin
from django.conf.urls import include
from django.conf.urls import url
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^api/insumo/$', views.InsumoViewSet.as_view()),
    url(r'^api/insumo_nombre/(?P<nombre>.+)/$',views.InsumoFiltroNombreViewSet.as_view()),
    url(r'^api/insumo_precio/(?P<precio>[0-9].+)/$',views.InsumoFiltroPrecioViewSet.as_view()),
    url(r'^api/contactoFinal/$',views.ContactoFinalViewSet.as_view())
]

urlpatterns=format_suffix_patterns(urlpatterns)
