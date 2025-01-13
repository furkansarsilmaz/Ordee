from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def tables(request):
    return HttpResponse('<h1> It is Tables </h1>')
