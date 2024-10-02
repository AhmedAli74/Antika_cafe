from django.shortcuts import render,redirect
from menu.models import Menu,Menu_iced
from .models import Contact
# Create your views here.
def home(request):
    menu=Menu.objects.all()[:4]
    menu_ice=Menu_iced.objects.all()[:4]
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        messages=request.POST['message']
        data=Contact()
        data.name=name
        data.mail=email
        data.message=messages
        data.save()
        return redirect('home:home')
    context={
        'menu':menu,
        'menu_ice':menu_ice
    }
    return render(request,'base.html',context)