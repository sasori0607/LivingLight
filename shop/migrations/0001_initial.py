# Generated by Django 4.0.2 on 2022-02-17 23:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug категории')),
                ('title', models.CharField(max_length=100, verbose_name='Имя категории')),
            ],
            options={
                'verbose_name': 'Категории',
                'verbose_name_plural': 'Категория',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug Товара')),
                ('amount', models.DecimalField(decimal_places=0, max_digits=5, verbose_name='Остаток(колл-во)')),
                ('title', models.CharField(max_length=100, verbose_name='Имя товара')),
                ('vendor_code', models.CharField(max_length=100, verbose_name='Артикул')),
                ('img', models.ImageField(upload_to='goods_img', verbose_name='Превью товара')),
                ('description', models.TextField(verbose_name='Описание')),
                ('prise_plate', models.DecimalField(decimal_places=0, max_digits=9, verbose_name='цена за пластину')),
                ('without_remote', models.DecimalField(decimal_places=0, max_digits=9, verbose_name='цена за модель без пульта')),
                ('with_remote', models.DecimalField(decimal_places=0, max_digits=9, verbose_name='цена за модель с пультом')),
                ('discount', models.DecimalField(decimal_places=0, max_digits=2, verbose_name='скидка')),
                ('newTrue', models.BooleanField(default=True, verbose_name='Является ли Новинкой?')),
                ('recommendation', models.BooleanField(default=True, verbose_name='Рекомендуем?')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category', verbose_name='Имя товара')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos')),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to='shop.products')),
            ],
        ),
    ]