from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Empleado, Insumo, ContactoFinal

class EmpleadoForm(ModelForm):


    class Meta:
        model = Empleado
        fields = ['rut','nombre','apellido','email','tipo','nombreUsuario','contraseña']

class InsumoForm(ModelForm):


    class Meta:
        model = Insumo
        fields= ['nombre','precio','descripcion','stock']

class ContactoFinalForm(ModelForm):

    class Meta:
        model = ContactoFinal
        fields = ['nombre', 'apellido', 'asunto', 'tipoCon', 'mensaje']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label= 'Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        
