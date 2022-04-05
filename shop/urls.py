from django.urls import path, include
from . import views
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', views.Shop_main.as_view(), name='shop_main'),
    path('<category>/<slug>', views.Shop_detail_page.as_view(), name='shop_detail'),
    #path('<slug>',  cache_page(60 * 15)(views.Shop_category.as_view()), name='shop_category'),
    path('<slug>',  views.Shop_category.as_view(), name='shop_category'),
    # path('delivery', views.delivery, name='delivery'),

]