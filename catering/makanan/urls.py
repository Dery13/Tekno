from django.contrib import admin
from django.urls import path, include

from makanan.views import *
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('menu/', tabelMenu, name='tabel-menu'),
    path('menu/tambah', tambah_menu, name='tambah_menu'),
    path('menu/view/<str:id>', view_menu, name='view_menu'),
    path('menu/edit_menu/<str:id>', edit_menu, name='edit_menu'),
    path('menu/delete_menu/<str:id>', delete_menu, name='delete_menu'),

    path('ckeditor/', include('ckeditor_uploader.urls')),
#     path('about/', about, name='about'),
#     path('contact/', contact, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
