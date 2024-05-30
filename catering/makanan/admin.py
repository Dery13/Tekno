from django.contrib import admin
from .models import *

class MenusAdmin(admin.ModelAdmin):
    list_display = ('menu', 'harga', 'deskripsi', 'date')

admin.site.register(Menus, MenusAdmin)
# Register your models here.
