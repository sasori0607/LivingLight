from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from shop.models import Order, Products, Category, Seo


class ShopMainTestCase(APITestCase):

    def setUp(self):
        self.category = Category.objects.create(
            slug='toys',
            title='TOYS'
        )
        self.category = Category.objects.create(
            slug='NOtoys',
            title='noTOYS'
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
        self.seo = Seo.objects.create(
            url='shop',
            title='Магазин главная',
            description='fgdfdgs dgf sf gdgfds gfd sgfds gfd dgf s',
            main_text='fgdfdgs dgf sf gdgfds gfd sgfds gfd dgf '
                      'fgdfdgs dgf sf gdgfds gfd sgfds gfd dgf '
                      'fgdfdgs dgf sf gdgfds gfd sgfds gfd dgf '
        )

    def test_shop_main(self):
        url = reverse('shop_main')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertTemplateUsed(response, 'shop/main_shop.html')
        self.assertEqual(response.context['seo'].title, self.seo.title)
        self.assertEqual(response.context['seo'].description, self.seo.description)
        self.assertEqual(response.context['seo'].main_text, self.seo.main_text)
        self.assertEqual(response.context['products'][0].slug, 'toy1')
        self.assertEqual(response.context['products'].last().slug, 'toy3')
        self.assertEqual(response.context['categorys'][0].slug, 'toys')
        self.assertEqual(response.context['categorys'].last().slug, 'NOtoys')


class ShopCategoryTestCase(APITestCase):

    def setUp(self):
        self.category = Category.objects.create(
            slug='toys',
            title='TOYS'
        )
        self.category = Category.objects.create(
            slug='NOtoys',
            title='noTOYS'
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
        self.seo = Seo.objects.create(
            url='toys',
            title='Магазин главная',
            description='fgdfdgs dgf sf gdgfds gfd sgfds gfd dgf s',
            main_text='fgdfdgs dgf sf gdgfds gfd sgfds gfd dgf '
                      'fgdfdgs dgf sf gdgfds gfd sgfds gfd dgf '
                      'fgdfdgs dgf sf gdgfds gfd sgfds gfd dgf '
        )

    def test_shop_main(self):
        url = reverse('shop_category', kwargs={'slug': 'toys'})
        response = self.client.get(url)
        print(response)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertTemplateUsed(response, 'shop/shop_category.html')
        self.assertEqual(response.context['seo'].title, self.seo.title)
        self.assertEqual(response.context['seo'].description, self.seo.description)
        self.assertEqual(response.context['seo'].main_text, self.seo.main_text)
        self.assertEqual(response.context['products'][0].slug, 'toy1')
        self.assertEqual(response.context['products'].last().slug, 'toy3')
        self.assertEqual(response.context['categorys'][0].slug, 'toys')
        self.assertEqual(response.context['categorys'].last().slug, 'NOtoys')
        url = reverse('shop_category', kwargs={'slug': 'toysssxvcss'})
        response = self.client.get(url)
        self.assertTemplateUsed(response, '404.html')


class ShopDetailTestCase(APITestCase):

    def setUp(self):
        self.category = Category.objects.create(
            slug='toys',
            title='TOYS'
        )
        self.category = Category.objects.create(
            slug='NOtoys',
            title='noTOYS'
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
        self.seo = Seo.objects.create(
            url='toys',
            title='Магазин главная',
            description='fgdfdgs dgf sf gdgfds gfd sgfds gfd dgf s',
            main_text='fgdfdgs dgf sf gdgfds gfd sgfds gfd dgf '
                      'fgdfdgs dgf sf gdgfds gfd sgfds gfd dgf '
                      'fgdfdgs dgf sf gdgfds gfd sgfds gfd dgf '
        )

    def test_shop_main(self):
        url = reverse('shop_detail', kwargs={'category': 'toys', 'slug': 'toy1'})
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertTemplateUsed(response, 'shop/shop_detail.html')
        self.assertEqual(response.context['product'].slug, 'toy1')
