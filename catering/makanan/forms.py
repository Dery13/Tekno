from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Menus

class MenuForms(forms.ModelForm):
    class Meta:
        model = Menus
        fields = ('menu', 'harga', 'deskripsi')
        widgets = {
             'menu' : forms.TextInput(attrs={'class':'form-control'}),
             'harga' : forms.TextInput(attrs={'class':'form-control'}),
             'deskripsi' :forms.Textarea(attrs={'class':'form-control'})
                }