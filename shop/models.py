# -*- coding: utf-8 -*-

from sorl.thumbnail import ImageField
from django.contrib.auth.models import User
from sorl.thumbnail.shortcuts import get_thumbnail
from pytils import translit
from shop.snippets import unique_slugify
from django.core.urlresolvers import reverse

from django.db import models

class  Settings(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=25)
    email = models.EmailField(max_length=40)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

class Page(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=25, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    active = models.BooleanField(default=False)
    position = models.PositiveSmallIntegerField(default=999)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = translit.slugify(self.name)
        unique_slugify(self, self.slug)
        super(Page, self).save()

class Producer(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __unicode__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    position = models.PositiveSmallIntegerField(default=999)
    active = models.BooleanField(default=False)
    position = models.PositiveSmallIntegerField(default=999)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('position', )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = translit.slugify(self.name)
        unique_slugify(self, self.slug)
        super(Category, self).save()

    def get_absolute_url(self):
        return reverse('category', args=[self.slug])

    def get_product_set_3(self):
        return   self.product_set.all()[:3]



class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)
    price = models.PositiveIntegerField()
    old_price = models.PositiveIntegerField(blank=True, null=True)
    hit_counter = models.PositiveIntegerField(default=0)
    qty = models.PositiveSmallIntegerField(default=0)
    producer = models.ForeignKey(Producer,blank=True, null=True, on_delete=models.SET_NULL)
    position = models.PositiveSmallIntegerField(default=999)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = translit.slugify(self.name)
        unique_slugify(self, self.slug)
        super(Product, self).save()

    class Meta:
        ordering = ('position', )

    def get_thumbnail_cat(self):
        images =self.productimage_set.all()[0]
        img = images.image
        height=210
        return unicode(get_thumbnail(img, 'x%i' % (height)).url)

class Collection(models.Model):
    name = models.CharField(max_length=20)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)
    accessories = models.ManyToManyField(Product,related_name='accessories', blank=True, null=True)
    products = models.ManyToManyField(Product,related_name='product', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    position = models.PositiveSmallIntegerField(default=999)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = translit.slugify(self.name)
        unique_slugify(self, self.slug)
        super(Collection, self).save()

class ProductImage(models.Model):
    product = models.ForeignKey(Product)
    image = ImageField(upload_to='product')
    position = models.PositiveSmallIntegerField(default=999)

    class Meta:
        ordering = ('position', )

    def __unicode__(self):
        return self.image.url

class ShippingMethod(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=1000, blank=True, null=True)
    active = models.BooleanField(default=False)
    price = models.PositiveIntegerField(default=0)
    days = models.PositiveIntegerField(blank=True, null=True)
    position = models.PositiveSmallIntegerField(default=999)

    def __unicode__(self):
        return self.name


class PaymentMethod(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=1000, blank=True, null=True)
    active = models.BooleanField(default=False)
    position = models.PositiveSmallIntegerField(default=999)

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
