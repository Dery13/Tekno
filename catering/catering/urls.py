from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static


from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('menu/', menu, name='menu'),
    path('dashboard/', include('makanan.urls')),
    path('dashboard/', include('users.urls')),

    # path('dashboard/', include('users.urls')),
#     path('about/', about, name='about'),
#     path('contact/', contact, name='contact'),
]