from django.shortcuts import render
from .models import Menu,Menu_iced
# Create your views here.
def menus(request):
    menuu=Menu.objects.all()
    iced_menuu=Menu_iced.objects.all()
    context={
        'menuu':menuu,
        'iced_menuu':iced_menuu
    }
    return render(request,'menu.html',context)