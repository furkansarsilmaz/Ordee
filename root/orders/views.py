from django.shortcuts import render
# Create your views here.
def order_menu(request):
    return render(request,'orders/order_menu.html')