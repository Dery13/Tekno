from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import User

class UserForms(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
             'username' : forms.TextInput(attrs={'class':'form-control'}),
             'password' : forms.TextInput(attrs={'class':'form-control'}),
                }