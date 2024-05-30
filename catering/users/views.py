from django.shortcuts import render, redirect
from .models import User
# Create your views here.


# def index(request):
#     template_name = "index.html"
#     menu = Menus.objects.all()
#     context = {
#         'title': 'Menu',
#         'menu': menu,
#     }
#     return render(request, template_name, context)

def dashboard(request):
    template_name = "back/dashboard.html"
    context = {
        'title': 'Dashboard'
    }

    return render(request, template_name, context)

def dashboard(request):
    template_name = "back/base.html"
    context = {
        'title': "Dashboard"
    }

    return render(request, template_name, context)
 
def menu(request):
    return render(request, 'menu.html')

def tabel_user(request):
    template_name = "back/users/tabel-user.html"
    user = User.objects.all()
    context = {
         'title': 'User',
         'user': user,
     }

    return render(request, template_name, context)

def tambah_user(request):
    template_name = "back/users/tambah_user.html"
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        User.objects.create(
            username = username,
            password = password,
        )
        return redirect(tabel_user)
    context = {
        'title':'Tambah User',
    }

    return render(request, template_name, context)

def view_user(request, id):
    template_name = "back/users/view_user.html"
    user = User.objects.get(id=id)
    context = {
        'title': 'view user',
        'user': user

    }
    return render(request, template_name, context)

def edit_user(request, id):
    template_name = "back/users/edit_user.html"  
    user = User.objects.get(id=id)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user.username = username
        user.password = password
        user.save()
        return redirect(tabel_user)
    context = {
        'title': 'edit user',
        'menu': user,

    }

    return render(request, template_name, context)

def delete_user(request, id):
    User.objects.get(id=id).delete()
    return redirect(tabel_user)

# def about(request):
#     return render(request, 'about.html')

# def contact(request):
#     return render(request, 'contact.html')