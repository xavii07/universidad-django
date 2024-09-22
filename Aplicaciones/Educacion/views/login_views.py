from django import forms
from  django.contrib.auth.forms import AuthenticationForm
from  django.contrib.auth.views import LoginView
from  django.shortcuts import redirect

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Usuario'},
    ), label='Usuario')

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
        label='Contraseña',
    )


class CustomLoginView(LoginView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super().get(request, *args, **kwargs)