from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.forms import fields, models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UsuarioForm(UserCreationForm):
    email = forms.EmailField(max_length=150)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        e = self.cleaned_data['email']
        if User.objects.filter(email=e).exists():
            raise ValidationError('Este e-mail {} já cadastrado!'.format(e))
        
        return e
