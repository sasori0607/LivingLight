from django.urls import path, include
from rest_framework.routers import SimpleRouter

from . import views
from .views import OrderViewSet

router = SimpleRouter()

router.register(r'allorders', OrderViewSet, basename='api')

urlpatterns = [
    path('add', views.basket_plus, name="add_basket"),
    path('down', views.basket_minus, name="down_basket"),
    path('my-cart', views.my_basket, name="my_basket"),
    path('order', views.order, name="order"),
    # path('delivery', views.delivery, name='delivery'),
]
urlpatterns += router.urls