# -*- coding: utf-8 -*-


from sorl.thumbnail import ImageField
from django.contrib.auth.models import User
from sorl.thumbnail.shortcuts import get_thumbnail


from django.db import models


class Settings(models.Model):
    title = models.CharField(max_length=60, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    tel = models.CharField(max_length=30)
    email = models.CharField(max_length=40)

    def __unicode__(self):
        return self.title

class Slider(models.Model):
    title = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=40, blank=True, null=True)
    image = models.ImageField(upload_to='slides')
    url = models.URLField(max_length=100)

    def __unicode__(self):
        return self.title

class HomeBanners(models.Model):
    title = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=40, blank=True, null=True)
    image = models.ImageField(upload_to='homebanners')
    url = models.URLField(max_length=100)

    def __unicode__(self):
        return self.title

class Pages(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=60, blank=True, null=True)
    content = models.TextField()
    slug = models.SlugField()
    menu = models.BooleanField(default=False)
    menu_name = models.CharField(max_length=25)

    def __unicode__(self):
        return self.title

class Producer(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()

    def __unicode__(self):
        return self.name

class Category(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField()
    description = models.TextField()

    def __unicode__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField()
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)
    collection = models.ForeignKey('Collection', blank=True, null=True, on_delete=models.SET_NULL)
    price = models.PositiveIntegerField()
    old_price = models.PositiveIntegerField(blank=True, null=True)
    hit_counter = models.PositiveIntegerField(default=0)
    qty = models.PositiveSmallIntegerField(default=0)
    producer = models.ForeignKey(Producer,blank=True, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.name

class Collection(models.Model):
    title = models.CharField(max_length=20)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)
    accessories = models.ManyToManyField(Product,related_name='accessories', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.title

class ProductImage(models.Model):
    product = models.ForeignKey(Product)
    title = models.CharField(blank=True, max_length=100, null=True)
    image = ImageField(upload_to='/product')
    position = models.PositiveSmallIntegerField(default=999)

    class Meta:
        ordering = ('position', )

    def __unicode__(self):
        return self.title


class ShippingMethod(models.Model):
    active = models.BooleanField(default=False)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=1000, blank=True, null=True)
    price = models.PositiveIntegerField()
    day = models.PositiveIntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.name

class PaymentMethod(models.Model):
    active = models.BooleanField(default=False)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return self.name

class Order(models.Model):
    STATUSES = (
        ('new', 'Новый'),
        ('confirm', 'Подтвержден'),
        ('service_shipping', 'Передача в службу доставки'),
        ('wait', 'Ожидается поставка'),
        ('self', 'Доставлен в точку самовывоза'),
        ('shipping', 'Доставка'),
        ('success', 'Завершен'),
        ('revoked', 'Отменен'),
        ('return', 'Возврат'),
        )
    status = models.CharField(max_length=20, default='new', choices=STATUSES)
    last_date = models.DateField(auto_now=True)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    name = models.CharField(max_length=40)
    address = models.TextField(blank=True, null=True)
    shipping_method = models.ForeignKey(ShippingMethod, blank=True, null=True, on_delete=models.SET_NULL)
    payment_method = models.ForeignKey(PaymentMethod, blank=True, null=True, on_delete=models.SET_NULL)
    date = models.DateField(auto_now_add=True)
    total = models.PositiveIntegerField()
    discount_code = models.CharField(max_length=15, blank=True, null=True)
    discount = models.FloatField( blank=True, null=True)
    voucher_code = models.CharField(max_length=15, blank=True, null=True)
    voucher_price = models.PositiveIntegerField(blank=True, null=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return '%s - %s' % (self.email, self.status)

class OrderItem(models.Model):
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product, blank=True, null=True, on_delete=models.SET_NULL )
    quantity = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField()

    def __unicode__(self):
        return self.product

class ClientProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    newsletter = models.BooleanField(default=False)
