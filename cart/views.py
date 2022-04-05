from django.core.exceptions import ValidationError
from django.http import JsonResponse, HttpResponse

from django.shortcuts import redirect, render
from django.template import Template

from shop.models import *


def product_sum(dict):
    sumator = 0
    for i in dict:
        sumator += int(dict[i])
    print(sumator)
    return sumator


def price_sum(dict, data_b):
    price_sum = 0
    print(dict, 'zzzzzzzzzzzzzzzzzzzzzz', data_b)
    for i in dict:
        data = data_b.filter(vendor_code=i[:-1])[0]
        if i[-1] == '1':
            price_sum += int(data.without_remote) * int(dict[i])
            print(data.without_remote)
        elif i[-1] == '2':
            price_sum += int(data.with_remote) * int(dict[i])
            print(data.with_remote)
        else:
            price_sum += int(data.prise_plate) * int(dict[i])
            print(data.prise_plate)
        print(price_sum)
    return price_sum


def basket_plus(request):

    data = request.POST
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
    if 'cart' not in request.session:
        request.session['cart'] = {}
    dict = request.session['cart']
    print(dict)
    print(data)
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
    return JsonResponse({'1': 'Hello from Django!'})
    # print(request.POST, 'FUCK')
    # myscript = '<script type="text/javascript"> alert("123") <script>'
    # myscript = Template(myscript)
    # return render(Template(myscript), template_name='shop/main_shop.html')
    #return redirect('/shop')



