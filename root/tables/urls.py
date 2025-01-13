from django.urls import path
from . import views

urlpatterns = [
    path('',views.tables,name='tables')
]