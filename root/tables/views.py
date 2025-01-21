from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Menu

# Create your views here.
@login_required(login_url="base.html")
def tables(request):
    print(request.user.is_authenticated)
    return render(request,'tables/tables.html')

def menu(request,table_id):
    products = Menu.objects.all()

    return render(request,'tables/menu.html',{'products' : products,'table_id':table_id})
