from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Menu, Order

@login_required(login_url="base.html")
def tables(request):
    print(request.user.is_authenticated)
    return render(request, 'tables/tables.html')

def menu(request, table_id):
    products = Menu.objects.all()
    menu_items = Order.objects.all()
    context = {
        'products': products,
        'table_id': table_id,
        'menu_item': menu_items 
    }
    return render(request, 'tables/menu.html',context)

def increase_order(request, menu_id):
    menu_item = get_object_or_404(Menu, id=menu_id)
    order, created = Order.objects.get_or_create(menu_item=menu_item)
    order.quantity += 1
    order.save()
    return redirect('menu', table_id=request.POST.get('table_id'))

def decrease_order(request, menu_id):
    menu_item = get_object_or_404(Menu, id=menu_id)
    order = get_object_or_404(Order, menu_item=menu_item)
    if order.quantity > 1:
        order.quantity -= 1
        order.save()
    else:
        order.delete()
    return redirect('menu', table_id=request.POST.get('table_id'))