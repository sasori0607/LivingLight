from django.contrib import messages
from django.core.exceptions import ValidationError
from django.http import JsonResponse, HttpResponse

from django.shortcuts import redirect, render
from django.template import Template
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.models import Token
from cart.serializers import OrderSerializers
from shop.models import *


def product_sum(dict):
    sumator = 0
    for i in dict:
        sumator += int(dict[i])
    return sumator


def price_sum(dict, data_b):
    price_sum = 0
    for i in dict:
        data = data_b.filter(vendor_code=i[:-1])[0]
        if i[-1] == '1':
            price_sum += int(data.without_remote) * int(dict[i])
        elif i[-1] == '2':
            price_sum += int(data.with_remote) * int(dict[i])
        else:
            price_sum += int(data.prise_plate) * int(dict[i])
        print(price_sum)
    return price_sum


def basket_plus(request):
    data = request.POST
    print(data)
    if 'cart' not in request.session:
        request.session['cart'] = {}
    dict = request.session['cart']
    if data['product'] not in dict:
        dict[data['product']] = data['val']
    else:
        dict[data['product']] = int(dict[data['product']]) + int(data['val'])
    request.session['cart'] = dict
    print(dict)
    request.session['sum'] = product_sum(request.session['cart'])
    sum = {'sum': request.session['sum'], 'amount': request.session['sum'], 'purchase_amount':  price_sum(dict, Products.objects)}
    return JsonResponse(sum)


def basket_minus(request):

    data = request.POST
    dict = request.session['cart']
    if int(dict[data['product']]) == 1:
        dict.pop(data['product'])
        amount = 0
        #удаления айтема с корзины добавить
    else:
        difference = int(dict[data['product']]) - int(data['val'])
        dict[data['product']] = difference
        amount = difference
    request.session['cart'] = dict
    request.session['sum'] = product_sum(request.session['cart'])
    sum = {'sum': request.session['sum'], 'amount': amount, 'purchase_amount':  price_sum(dict, Products.objects)}
    print(dict)
    return JsonResponse(sum)


def my_basket(request):
    cart = request.session['cart']
    data_b = Products.objects
    print(data_b)
    answer = {}
    for i in cart:
        print(i)
        print(i[:-1])
        answer[i] = {}
        data = data_b.filter(vendor_code=i[:-1])[0]
        print(data.category)
        answer[i]['url'] = f'{data.category}/{data.slug}'
        answer[i]['title'] = f'{data.title}'
        answer[i]['img'] = f'{data.img.url}'
        if i[-1] == '1':
            answer[i]['price'] = f'{data.without_remote}'
            answer[i]['type'] = 'Классический комплект'
            answer[i]['type_kof'] = '1'
        elif i[-1] == '2':
            answer[i]['price'] = f'{data.with_remote}'
            answer[i]['type'] = 'Комплект с пультом'
            answer[i]['type_kof'] = '2'
        else:
            answer[i]['price'] = f'{data.prise_plate}'
            answer[i]['type'] = 'Только пластина'
            answer[i]['type_kof'] = '0'
        answer[i]['amount'] = f'{cart[i]}'
        answer[i]['vendor_code'] = f'{data.vendor_code}'
    answer['purchase_amount'] = price_sum(cart, data_b)
    return JsonResponse(answer)


def order(request):

    str = ''
    data_b = Products.objects
    for i in request.session['cart']:
        data = data_b.filter(vendor_code=i[:-1])[0]
        if i[-1] == '1':
            price = f'{data.without_remote}'
            product_type = 'Классический комплект'
        elif i[-1] == '2':
            price = f'{data.with_remote}'
            product_type = 'Комплект с пультом'
        else:
            price = f'{data.prise_plate}'
            product_type = 'Только пластина'
        print(str)
        str += f'{data.title} ({product_type}) ценной {price} \n'
    inp = request.POST
    ord = Order()
    ord.order = str
    ord.name = inp['name']
    ord.town = inp['town']
    ord.department = inp['department']
    ord.email = inp['email']
    ord.tel = inp['tel']
    ord.comment = inp['comment']
    ord.save()
    request.session['cart'] = {}
    request.session['sum'] = 0


    messages.success(request, f'{ord.name} ваша заявка принята! Мы свяжемся с вами в ближайшее время.')
    return JsonResponse({'1': 'True'})


class OrderViewSet(ModelViewSet):


    permissions_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    queryset = queryset.filter(status=True)
    serializer_class = OrderSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ['status']
    search_fields = ['name', 'town', 'tel']







