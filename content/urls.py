from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    # path('delivery', views.delivery, name='delivery'),
    path('about', views.About.as_view(), name='about'),
    path('for-you', views.Contacts.as_view(), name='contacts'),
]
