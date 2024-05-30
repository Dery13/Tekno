from django.contrib import admin
from django.urls import path, include

from users.views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('users/', tabel_user, name='tabel_user'),
    path('users/tambah', tambah_user, name='tambah_user'),
    path('user/view/<str:id>', view_user, name='view_user'),
    path('user/edit_user/<str:id>', edit_user, name='edit_user'),
    path('user/delete_menu/<str:id>', delete_user, name='delete_user'),
    # path('user/', users, name='tabel-user'),
#     path('about/', about, name='about'),
#     path('contact/', contact, name='contact'),
]
