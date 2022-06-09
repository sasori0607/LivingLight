import json
from collections import OrderedDict

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from cart.serializers import OrderSerializers
from cart.views import product_sum, price_sum
from shop.models import Order, Products, Category
from django.contrib.auth.models import User


class OrderApiTestCase(APITestCase):
    def test_get(self):
        order_1 = Order.objects.create(
            name='Пупков Генадий',
            town='г.Умань',
            department='Отделение новой почты №6',
            email='some@gmail.com',
            tel=',+380950319896',
            comment='Хочу',
            order='++',
            status=True
        )
        order_2 = Order.objects.create(
            name='Бойко Никита',
            town='г.Харьков',
            department='Отделение новой почты №13',
            email='some123@gmail.com',
            tel=',+380950359875',
            comment='Хочу',
            order='--------',
            status=False
        )
        order_3 = Order.objects.create(
            name='Пентюк Суперолвич',
            town='г.Киев',
            department='Отделение новой почты №32',
            email='testtest@gmail.com',
            tel=',+380950359875',
            comment='',
            order='СЮДА СЮДА',
            status=True
        )
        user = User.objects.create_user(username='sasori', password='sasori')
        print(user.username)
        token = Token.objects.create(user=User.objects.all().filter(username='sasori')[0])
        print(token)

        unser = [OrderedDict(
            [('id', 1), ('name', 'Пупков Генадий'), ('town', 'г.Умань'), ('department', 'Отделение новой почты №6'),
             ('email', 'some@gmail.com'), ('tel', ',+380950319896'), ('comment', 'Хочу'), ('order', '++'),
             ('status', True)]), \
            OrderedDict([('id', 3), ('name', 'Пентюк Суперолвич'), ('town', 'г.Киев'),
                         ('department', 'Отделение новой почты №32'),
                         ('email', 'testtest@gmail.com'), ('tel', ',+380950359875'), ('comment', ''),
                         ('order', 'СЮДА СЮДА'), ('status', True)
                         ])]

        url = reverse('api-list')
        response = self.client.get(url, HTTP_AUTHORIZATION=f'Token {token}')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(unser, response.data)


class SumAmountTestCase(APITestCase):
    def test_product_sum(self):
        test_dict_1 = {'product1': '1', 'product3': 2, 'product2': '12'}
        answer_1 = 15
        test_dict_2 = {'product12': '2', 'product33': 13, 'product28': '26'}
        answer_2 = 41
        test_sum_1 = product_sum(test_dict_1)
        test_sum_2 = product_sum(test_dict_2)
        self.assertEqual(answer_1, test_sum_1)
        self.assertEqual(answer_2, test_sum_2)


class SumPriceTestCase(APITestCase):

    def test_data(self):
        category = Category.objects.create(
            slug='toys',
            title='TOYS'
        )
        product_1 = Products.objects.create(
            slug='toy1',
            amount='13',
            title='грушка 1',
            category=category,
            vendor_code='951952',
            img='img/try2.png',
            description='BLAAAAAAAAAAAAAAAA ddsad',
            prise_plate='100',
            without_remote='200',
            with_remote='300',
            discount='5',
            discountCheck=True,
            newTrue=True,
        )
        product_2 = Products.objects.create(
            slug='toy2',
            amount='45',
            title='игрушка 2',
            category=category,
            vendor_code='455226',
            img='img/try2.png',
            description='иссчимсчи см чисимч',
            prise_plate='150',
            without_remote='250',
            with_remote='350',
            discount='0',
            discountCheck=True,
            newTrue=True,
            recommendation=True
        )

        test_dict_order_1 = {'4552260': '1', '4552261': 1, '4552262': '2'}
        sum_1 = price_sum(test_dict_order_1, Products.objects.all())
        test_dict_order_2 = {'4552260': '10', '9519521': 1, '4552262': '2'}
        sum_2 = price_sum(test_dict_order_2, Products.objects.all())
        self.assertEqual(sum_1, 1100)
        self.assertEqual(sum_2, 2400)


class BasketTestCase(APITestCase):

    def setUp(self):
        self.category = Category.objects.create(
            slug='toys',
            title='TOYS'
        )
        self.product_1 = Products.objects.create(
            slug='toy1',
            amount='13',
            title='грушка 1',
            category=self.category,
            vendor_code='951952',
            img='img/try2.png',
            description='BLAAAAAAAAAAAAAAAA ddsad',
            prise_plate='100',
            without_remote='200',
            with_remote='300',
            discount='5',
            discountCheck=True,
            newTrue=True,
        )
        self.product_2 = Products.objects.create(
            slug='toy2',
            amount='45',
            title='игрушка 2',
            category=self.category,
            vendor_code='455226',
            img='img/try2.png',
            description='иссчимсчи см чисимч',
            prise_plate='150',
            without_remote='250',
            with_remote='350',
            discount='0',
            discountCheck=True,
            newTrue=True,
            recommendation=True
        )
        self.product_3 = Products.objects.create(
            slug='toy3',
            amount='45',
            title='игрушка 2',
            category=self.category,
            vendor_code='455226',
            img='img/try2.png',
            description='иссчимсчи см чисимч',
            prise_plate='150',
            without_remote='250',
            with_remote='350',
            discount='0',
            discountCheck=True,
            newTrue=True,
            recommendation=True
        )

    def test_basket_plus(self):
        url = reverse('add_basket')
        data = {
            'product': '9519520',
            'val': '3'
        }
        response = self.client.post(url, data=data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(3, response.json()['sum'])
        self.assertEqual(3, response.json()['amount'])
        self.assertEqual(300, response.json()['purchase_amount'])

        data = {
            'product': '9519521',
            'val': '2'
        }
        response = self.client.post(url, data=data)

        print(response.json())
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(5, response.json()['sum'])
        self.assertEqual(5, response.json()['amount'])
        self.assertEqual(700, response.json()['purchase_amount'])

        data = {
            'product': '9519520',
            'val': '1'
        }
        response = self.client.post(url, data=data)

        print(response.json())
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(6, response.json()['sum'])
        self.assertEqual(6, response.json()['amount'])
        self.assertEqual(800, response.json()['purchase_amount'])

    def test_basket_minus(self):
        url = reverse('add_basket')
        data = {
            'product': '9519520',
            'val': '3'
        }
        self.client.post(url, data=data)
        data = {
            'product': '9519521',
            'val': '1'
        }
        self.client.post(url, data=data)

        url = reverse('down_basket')
        data = {
            'product': '9519520',
            'val': '1'
        }
        response = self.client.post(url, data=data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(3, response.json()['sum'])
        self.assertEqual(2, response.json()['amount'])
        self.assertEqual(400, response.json()['purchase_amount'])

        data = {
            'product': '9519520',
            'val': '2'
        }
        response = self.client.post(url, data=data)
        print(response.json(), '++++++')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(1, response.json()['sum'])
        self.assertEqual(0, response.json()['amount'])
        self.assertEqual(200, response.json()['purchase_amount'])
        data = {
            'product': '9519521',
            'val': '2'
        }
        response = self.client.post(url, data=data)
        print(response.json(), '++++++')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(0, response.json()['sum'])
        self.assertEqual(0, response.json()['amount'])
        self.assertEqual(0, response.json()['purchase_amount'])

    def test_my_basket(self):
        url = reverse('add_basket')
        data = {
            'product': '9519520',
            'val': '3'
        }
        self.client.post(url, data=data)

        url = reverse('add_basket')
        data = {
            'product': '4552261',
            'val': '3'
        }
        self.client.post(url, data=data)

        url = reverse('add_basket')
        data = {
            'product': '4552262',
            'val': '3'
        }
        self.client.post(url, data=data)

        url = reverse('my_basket')
        response = self.client.post(url)

        data = {'9519520': {'url': 'toys/toy1', 'title': 'грушка 1', 'img': '/mediafiles/img/try2.png', 'price': '100',
                            'type': 'Только пластина', 'type_kof': '0', 'amount': '3', 'vendor_code': '951952'},
                '4552261': {'url': 'toys/toy2', 'title': 'игрушка 2', 'img': '/mediafiles/img/try2.png', 'price': '250',
                            'type': 'Классический комплект', 'type_kof': '1', 'amount': '3', 'vendor_code': '455226'},
                '4552262': {'url': 'toys/toy2', 'title': 'игрушка 2', 'img': '/mediafiles/img/try2.png', 'price': '350',
                            'type': 'Комплект с пультом', 'type_kof': '2', 'amount': '3', 'vendor_code': '455226'},
                'purchase_amount': 2100}

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(data, response.json())


class OrderTestCase(APITestCase):
    def setUp(self):
        order_2 = Order.objects.create(
            name='Бойко Никита',
            town='г.Харьков',
            department='Отделение новой почты №13',
            email='some123@gmail.com',
            tel=',+380950359875',
            comment='Хочу',
            order='--------',
            status=False
        )
        order_3 = Order.objects.create(
            name='Пентюк Суперолвич',
            town='г.Киев',
            department='Отделение новой почты №32',
            email='testtest@gmail.com',
            tel=',+380950359875',
            comment='',
            order='СЮДА СЮДА',
            status=True
        )

        self.category = Category.objects.create(
            slug='toys',
            title='TOYS'
        )
        self.product_1 = Products.objects.create(
            slug='toy1',
            amount='13',
            title='грушка 1',
            category=self.category,
            vendor_code='951952',
            img='img/try2.png',
            description='BLAAAAAAAAAAAAAAAA ddsad',
            prise_plate='100',
            without_remote='200',
            with_remote='300',
            discount='5',
            discountCheck=True,
            newTrue=True,
        )
        self.product_2 = Products.objects.create(
            slug='toy2',
            amount='45',
            title='игрушка 2',
            category=self.category,
            vendor_code='455226',
            img='img/try2.png',
            description='иссчимсчи см чисимч',
            prise_plate='150',
            without_remote='250',
            with_remote='350',
            discount='0',
            discountCheck=True,
            newTrue=True,
            recommendation=True
        )
        self.product_3 = Products.objects.create(
            slug='toy3',
            amount='45',
            title='игрушка 2',
            category=self.category,
            vendor_code='455226',
            img='img/try2.png',
            description='иссчимсчи см чисимч',
            prise_plate='150',
            without_remote='250',
            with_remote='350',
            discount='0',
            discountCheck=True,
            newTrue=True,
            recommendation=True
        )

    def test_order(self):
        url = reverse('add_basket')
        data = {
            'product': '9519520',
            'val': '3'
        }
        self.client.post(url, data=data)
        data = {
            'product': '9519521',
            'val': '2'
        }
        self.client.post(url, data=data)
        data = {
            'product': '9519522',
            'val': '1'
        }
        self.client.post(url, data=data)

        data = {
            'name': 'Пупков Генадий',
            'town': 'г.Умань',
            'department': 'Отделение новой почты №6',
            'email': 'some@gmail.com',
            'tel': '+380950319896',
            'comment': 'Хочу',
            'order': '++',
            'status': True
        }
        url = reverse('order')
        response = self.client.post(url, data=data)
        print(response)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        last_order = Order.objects.filter(status=True).last()
        self.assertEqual('Пупков Генадий', last_order.name)
        self.assertEqual('+380950319896', last_order.tel)
        self.assertEqual('г.Умань', last_order.town)
        self.assertEqual('Отделение новой почты №6', last_order.department)
        data_order = 'грушка 1 (Только пластина) ценной 100 \n' \
               'грушка 1 (Классический комплект) ценной 200 \n' \
               'грушка 1 (Комплект с пультом) ценной 300 \n'
        self.assertEqual(data_order, last_order.order)
