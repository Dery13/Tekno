from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from makanan.models import Menus

# Create your views here.
@login_required
def dashboard(request):
    template_name = "back/dashboard.html"
    context = {
        'title': 'Dashboard',
    }

    return render(request, template_name, context)

def index(request):
    template_name = "index.html"
    menu = Menus.objects.all().order_by('-date')[:3]
    context = {
        'title': 'Dapurnya Nini',
        'menu': menu,
    }
    return render(request, template_name, context)
 
def menu(request):
    menu = Menus.objects.all()
    context = {
        'title' : 'Menu',
        'menu': menu,
    }
    return render(request, 'menu.html', context)

def login(request):   
    if request.user.is_authenticated:
        print('sudah login')
        return redirect(dashboard)
     
    template_name = "account/login.html"
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print('username benar')
            auth_login(request, user)
            return redirect(dashboard)
        else:
            print('username salah')

    context = {
        'title': 'Login'
    }

    return render(request, template_name, context)

def logout_view(request):
    logout(request)
    return redirect(login)



# def about(request):
#     return render(request, 'about.html')

# def contact(request):
#     return render(request, 'contact.html')