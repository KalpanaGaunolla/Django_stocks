from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='stocks_home'),
    path('about/',views.about,name='stocks_about'),
    path('add_stock/',views.add_stock,name='add_stock'),
    path('delete/<stock_id>',views.delete,name='delete'),
    path('delete_stock/',views.delete_stock,name='delete_stock'),

]