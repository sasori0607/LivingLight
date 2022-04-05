from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('delivery', views.delivery, name='delivery'),
    path('about',  views.About.as_view() , name='about'),
    path('contacts',  views.Contacts.as_view() , name='contacts'),
]