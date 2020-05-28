# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields =['username',
                 'first_name',
                 'email',
                 'password'
                 ]
        error_messages = {
            'username': {'required': 'Este campo é obrigatório', 'unique':'Usuário já cadastrado. Escolha outro username'},
            'first_name': {'required': 'Este campo é obrigatório'},
            'email': {'required': 'Este campo é obrigatório', 'invalid':'Digite um e-mail Válido'},
            'password': {'required': 'Este campo é obrigatório'}
        }