from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
# Create your views here.

def is_operator(user):
    if user.groups.filter(name='Operator').exists():
        return True
    else:
        return False

@login_required
def dashboard(request):
    if request.user.groups.filter(name='Operator').exists():
        request.session['is_operator'] = 'operator'
    template_name = "back/dashboard.html"
    context = {
        'title': 'Dashboard'
    }

    return render(request, template_name, context)

# def dashboard(request):
#     template_name = "back/base.html"
#     context = {
#         'title': "Dashboard"
#     }

#     return render(request, template_name, context)
 
def menu(request):
    return render(request, 'menu.html')

@login_required
@user_passes_test(is_operator)
def tabel_user(request):
    template_name = "back/users/tabel-user.html"
    user = User.objects.all()
    context = {
         'title': 'User',
         'user': user,
     }

    return render(request, template_name, context)

@login_required
@user_passes_test(is_operator)
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

@login_required
@user_passes_test(is_operator)
def view_user(request, id):
    template_name = "back/users/view_user.html"
    user = User.objects.get(id=id)
    context = {
        'title': 'view user',
        'user': user

    }
    return render(request, template_name, context)

@login_required
@user_passes_test(is_operator)
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

@login_required
@user_passes_test(is_operator)
def delete_user(request, id):
    User.objects.get(id=id).delete()
    return redirect(tabel_user)
