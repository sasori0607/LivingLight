from django.test import TestCase
from shop.models import Products, Category



class CategoryModelTest(TestCase):

    def setUp(self):
        self.my_category = Category.objects.create(
            slug='toys',
            title='Toys333'
        )
        self.category = Category.objects.create(
            slug='NOtoys',
            title='noTOYS'
        )

    def test_get_absolute_url(self):
        category = Category.objects.all()[0]
        self.assertEquals(category.get_absolute_url(), '/shop/toys')


class ProductsModelTest(TestCase):

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

    def test_get_absolute_url(self):
        product = Products.objects.all()[0]
        self.assertEquals(product.get_absolute_url(), '/shop/NOtoys/toy1')
        product = Products.objects.all()[1]
        self.assertEquals(product.get_absolute_url(), '/shop/NOtoys/toy2')
