from django.shortcuts import render
from tables.models import Menu,Order 
# Create your views here.
def order_menu(request):
    return render(request,'orders/order_menu.html')

def order_menu(request):
    orders = Order.objects.all()
    return render(request, 'orders/order_menu.html', {'menu_items': orders})