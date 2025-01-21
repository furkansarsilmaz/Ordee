from django.urls import path
from . import views

urlpatterns = [
    path('',views.tables,name='tables'),
    path('<int:table_id>/menu', views.menu, name='menu'),
    path('increase_order/<int:menu_id>/', views.increase_order, name='increase_order'),
    path('decrease_order/<int:menu_id>/', views.decrease_order, name='decrease_order'),
]