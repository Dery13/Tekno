from django.shortcuts import render
from makanan.models import Menus
# Create your views here.


def index(request):
    template_name = "index.html"
    menu = Menus.objects.all()
    context = {
        'title': 'Menu',
        'menu': menu,
    }
    return render(request, template_name, context)
 
def menu(request):
    return render(request, 'menu.html')


# def about(request):
#     return render(request, 'about.html')

# def contact(request):
#     return render(request, 'contact.html')