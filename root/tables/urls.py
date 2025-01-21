from django.urls import path
from . import views

urlpatterns = [
    path('',views.tables,name='tables'),
    path('<int:table_id>/menu',views.menu,name='menu'),
]