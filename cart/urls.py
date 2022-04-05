from django.urls import path, include
from . import views

urlpatterns = [
    path('add', views.basket_plus),
    path('down', views.basket_minus),
    path('my-cart', views.my_basket),
    path('order', views.order, name="order"),
    # path('delivery', views.delivery, name='delivery'),

]