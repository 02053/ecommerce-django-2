from django import forms
from .models import Buyer


class RegisterBuyerForm(forms.ModelForm):
    username = forms.TextInput()
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Ingrese su contraseña')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Confirme su contraseña')

    class Meta:
        model = Buyer
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'})
        }
        labels = {
            'username': 'Ingrese su nombre de usuario',
        }


class LoginBuyerForm(forms.ModelForm):
    username = forms.TextInput()
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Ingrese su contraseña')

    class Meta:
        model = Buyer
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'})
        }
        labels = {
            'username': 'Ingrese su nombre de usuario',
        }
