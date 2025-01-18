from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url="base.html")
def tables(request):
    print(request.user.is_authenticated)
    return render(request,'tables/tables.html')