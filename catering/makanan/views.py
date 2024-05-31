from django.shortcuts import render, redirect
from .models import Menus
from .forms import MenuForms
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.

def is_operator(user):
    if user.groups.filter(name='Operator').exists():
        return True
    else:
        return False

@login_required
def dashboard(request):
    template_name = "back/dashboard.html"
    context = {
        'title': 'Dashboard'
    }

    return render(request, template_name, context)
 
def menu(request):
    return render(request, 'menu.html')


@login_required
def tabelMenu(request):
    menu = Menus.objects.all()
    form = MenuForms()
    return render(request, 'back/menu/tabel-menu.html', {'menu' : menu, 'form': form})

@login_required
def tambah_menu(request):
    if request.method == "POST":
        form = MenuForms(request.POST)
        if form.is_valid():
            form.save()
        return redirect(tabelMenu)
    else:
        form = MenuForms()

    return render(request, 'back/menu/tambah_menu.html', {'form': form})

@login_required
def view_menu(request, id):
    template_name = "back/menu/view_menu.html"
    menu = Menus.objects.get(id=id)
    context = {
        'title': 'view menu',
        'menu': menu

    }
    return render(request, template_name, context)

@login_required
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

@login_required
def delete_menu(request, id):
    Menus.objects.get(id=id).delete()
    return redirect(tabelMenu)