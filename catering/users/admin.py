from django.contrib import admin
from .models import *

class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'date')

admin.site.register(User, UsersAdmin)
