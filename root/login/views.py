from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import auth
from django.contrib import messages
# Create your views here.

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.aauthenticate(username= username , password= password)
        if user is not None :
            auth.login(request,user)
            messages.add_message(request,messages.SUCCESS,'Approved')
            return redirect('tables')
        else:
            messages.add_message(request,messages.ERROR,'Failed')
            return redirect('')
    else:
        return render(request,'base.html')
        
    """
    return render(request,'base.html')
    """