from django.conf import settings
from django.db import models
from django.urls import reverse
from PIL import Image


class Category(models.Model):

    slug = models.SlugField(unique=True, verbose_name="Slug категории")
    title = models.CharField(max_length=100, verbose_name="Имя категории")

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категория'

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        reverse('shop_category', kwargs={'slug': self.category.slug})


class Products(models.Model):
    slug = models.SlugField(unique=True, verbose_name="Slug Товара")
    amount = models.DecimalField(max_digits=5, decimal_places=0, verbose_name='Остаток(колл-во)')
    title = models.CharField(max_length=100, verbose_name="Имя товара")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    vendor_code = models.CharField(max_length=100, verbose_name="Артикул")
    img = models.ImageField(upload_to='goods_img', verbose_name='Превью товара')
    description = models.TextField(verbose_name='Описание')
    prise_plate = models.DecimalField(max_digits=9, decimal_places=0, verbose_name='цена за пластину')
    without_remote = models.DecimalField(max_digits=9, decimal_places=0, verbose_name='цена за модель без пульта')
    with_remote = models.DecimalField(max_digits=9, decimal_places=0, verbose_name='цена за модель с пультом')
    discount = models.DecimalField(max_digits=2, decimal_places=0, verbose_name='скидка')
    discountCheck = models.BooleanField(verbose_name='Есть ли скидка?', default=False)
    newTrue = models.BooleanField(verbose_name='Является ли Новинкой?', default=True)
    recommendation = models.BooleanField(verbose_name='Рекомендуем?', default=False)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('shop_detail', kwargs={'slug': self.slug, 'category': self.category})


class Seo(models.Model):
    url = models.SlugField(unique=True, verbose_name="Страница")
    title = models.CharField(max_length=120, verbose_name="Блок title")
    description = models.CharField(max_length=150, verbose_name="Блок description")
    main_text = models.TextField(verbose_name='Основной Сео текст страницы')

    class Meta:
        verbose_name = 'Seo'
        verbose_name_plural = 'Seo'


class Order(models.Model):
    name = models.CharField(max_length=180, verbose_name="ФИО")
    town = models.CharField(max_length=180, verbose_name="Город")
    department = models.CharField(max_length=180, verbose_name="Отделение новой почты")
    email = models.CharField(max_length=180, verbose_name="Email", null=True)
    tel = models.CharField(max_length=180, verbose_name="Телефон")
    comment = models.TextField(verbose_name="Коментарий", null=True)
    order = models.TextField(verbose_name="Заказ")

class Photo(models.Model):

    image = models.ImageField(upload_to='photos')
    gallery = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='pictures')










