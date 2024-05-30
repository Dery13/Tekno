from django.shortcuts import render, redirect
from .models import Menus
from .forms import MenuForms
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


# def tabelMenu(request):
#     template_name = "back/menu/tabel-menu.html"
#     menu = Menus.objects.all()
#     form = MenuForms()
#     context = {
#          'title': 'Menu',
#          'menu': menu,
#          'form' : form,
#      }

#     return render(request, template_name, context)

def tabelMenu(request):
    menu = Menus.objects.all()
    form = MenuForms()
    return render(request, 'back/menu/tabel-menu.html', {'menu' : menu, 'form': form})

def tambah_menu(request):
    if request.method == "POST":
        form = MenuForms(request.POST)
        if form.is_valid():
            form.save()
        return redirect(tabelMenu)
    else:
        form = MenuForms()

    return render(request, 'back/menu/tambah_menu.html', {'form': form})

# def tambah_menu(request):
#     template_name = "back/menu/tambah_menu.html"
#     if request.method == "POST":
#         menu = request.POST.get('menu')
#         harga = request.POST.get('harga')
#         deskripsi = request.POST.get('deskripsi')
#         Menus.objects.create(
#             menu = menu,
#             harga = harga,
#             deskripsi = deskripsi,
#         )
#         return redirect(tabelMenu)
#     context = {
#         'title':'Tambah Menu',
#     }

#     return render(request, template_name, context)

def view_menu(request, id):
    template_name = "back/menu/view_menu.html"
    menu = Menus.objects.get(id=id)
    context = {
        'title': 'view menu',
        'menu': menu

    }
    return render(request, template_name, context)

def edit_menu(request, id):
    template_name = "back/menu/edit_menu.html"  
    menus = Menus.objects.get(id=id)
    if request.method == "POST":
        menu = request.POST.get('menu')
        harga = request.POST.get('harga')
        deskripsi = request.POST.get('deskripsi')
        menus.menu = menu
        menus.harga = harga
        menus.deskripsi = deskripsi
        menus.save()
        return redirect(tabelMenu)
    context = {
        'title': 'edit menu',
        'menu': menus,

    }

    return render(request, template_name, context)

def delete_menu(request, id):
    Menus.objects.get(id=id).delete()
    return redirect(tabelMenu)

# def about(request):
#     return render(request, 'about.html')

# def contact(request):
#     return render(request, 'contact.html')