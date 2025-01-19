from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Menu

# Create your views here.
@login_required(login_url="base.html")
def tables(request):
    print(request.user.is_authenticated)
    return render(request,'tables/tables.html')

def menu(request):
    products = Menu.objects.all()
    return render(request,'tables/menu.html',{'products' : products})