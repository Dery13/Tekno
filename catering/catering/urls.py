from django.contrib import admin
from django.urls import path

from makanan.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index, name='index'),
    path('menu/', menu, name='menu'),
#     path('about/', about, name='about'),
#     path('contact/', contact, name='contact'),
]
