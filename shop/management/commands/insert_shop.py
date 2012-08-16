# -*- coding: utf-8 -*-

import sys
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import NoArgsCommand
from django.core.files import File
import random

from shop.models import *

def get_status(name, status):
    if status:
        status = 'done'
    else:
        status = 'already exists '
    print 'Inserting '+name+ ' -- ' +status

def insert_settings():
    try:
        settings = Settings.objects.get(pk=1)
        get_status('Settings', False)
    except ObjectDoesNotExist:
        s = Settings.objects.create(
            title = u'Интернет магазин',
            description = u'магазин электорнных гаджетов',
            phone = u'8 (800) 544 44 11',
            email = u'fi11@nm.ru',
            active = True,
        )
        get_status('Settings', True)

def insert_cat():
    try:
        cat = Category.objects.get(pk=1)
        get_status('Category', False)
    except ObjectDoesNotExist:
        titles=(
            u'Телефоны',
            u'Планшеты',
            u'Ноутбуки',
            u'Фототехника',
            u'Консоли',
            u'Акссесуары',
            )
        for t in titles:
            c = Category.objects.create(
                name = t,
                description = u'Текст описания категории в оснавном для СЕО. Пользователь это даже не будет четать, но поисковику может пригодиться',
            )
        get_status('Category', True)

def insert_collections():
    try:
        cat = Collection.objects.get(pk=1)
        get_status('Collections', False)
    except ObjectDoesNotExist:
        names = (
            u'Айфоны',
            u'Мастхев',
            u'Фигня',
        )
        for n in names:
            c = Collection.objects.create(
                name = n,
                description = u'тестовая коллекция для проверки',
                category = Category.objects.get(pk=1)
            )
        get_status('Collections', True)

def insert_producer():
    try:
        cat = Producer.objects.get(pk=1)
        get_status('Producers', False)
    except ObjectDoesNotExist:
        names = (
            u'Apple',
            u'Sumsung',
            u'China podval inc',
            )
        for n in names:
            c = Producer.objects.create(
                name = n,
                description = u'Описание фирмы производителя. Данный текст преднозначен воснавном для поискового продвижения.',
            )
        get_status('Producers', True)

def insert_products():

    try:
        p = Product.objects.get(pk=1)
        get_status('Products', False)
    except ObjectDoesNotExist:
            cat =Category.objects.all()
            prod =Producer.objects.all()
            products = (
               {'name': u'Apple iPhone 4s 64gb', 'description': u'У данного Apple iPhone 4 32Gb, множество преимуществ, но самым явным, является новый ультрасовременный дисплей, повышенной четкости – Retina. Как и следовало ожидать, в данном Iphone, огромное количество функций, с которыми справится даже маленький ребенок!Именно на это и рассчитывал создатель компании Apple – Стив Джобс!Среди функциональных способностей, можно также подчеркнуть «мультитач», функция, которая полностью перевернула мир сенсорных смартфонов! ',
                'price': 27000, 'old_price': 30000, 'category': cat[0], 'qty': 99,  'producer': prod[0]},
               {'name': u'Apple iPhone 4s 32gb', 'description': u'У данного Apple iPhone 4 32Gb, множество преимуществ, но самым явным, является новый ультрасовременный дисплей, повышенной четкости – Retina. Как и следовало ожидать, в данном Iphone, огромное количество функций, с которыми справится даже маленький ребенок!Именно на это и рассчитывал создатель компании Apple – Стив Джобс!Среди функциональных способностей, можно также подчеркнуть «мультитач», функция, которая полностью перевернула мир сенсорных смартфонов! ',
                'price': 26000, 'old_price': 29000, 'category': cat[0], 'qty': 99,  'producer': prod[0]},
               {'name': u'Apple iPhone 4s 16gb', 'description': u'У данного Apple iPhone 4 32Gb, множество преимуществ, но самым явным, является новый ультрасовременный дисплей, повышенной четкости – Retina. Как и следовало ожидать, в данном Iphone, огромное количество функций, с которыми справится даже маленький ребенок!Именно на это и рассчитывал создатель компании Apple – Стив Джобс!Среди функциональных способностей, можно также подчеркнуть «мультитач», функция, которая полностью перевернула мир сенсорных смартфонов! ',
                'price': 24000, 'old_price': 0,  'category': cat[0], 'qty': 0,  'producer': prod[0]},
               {'name': u'Apple iPhone 3g 16gb', 'description': u'У данного Apple iPhone 4 32Gb, множество преимуществ, но самым явным, является новый ультрасовременный дисплей, повышенной четкости – Retina. Как и следовало ожидать, в данном Iphone, огромное количество функций, с которыми справится даже маленький ребенок!Именно на это и рассчитывал создатель компании Apple – Стив Джобс!Среди функциональных способностей, можно также подчеркнуть «мультитач», функция, которая полностью перевернула мир сенсорных смартфонов! ',
                'price': 14000, 'old_price': 0,  'category': cat[0], 'qty': 0,  'producer': prod[0]},
               {'name': u'Apple iPhone 4s 16gb', 'description': u'У данного Apple iPhone 4 32Gb, множество преимуществ, но самым явным, является новый ультрасовременный дисплей, повышенной четкости – Retina. Как и следовало ожидать, в данном Iphone, огромное количество функций, с которыми справится даже маленький ребенок!Именно на это и рассчитывал создатель компании Apple – Стив Джобс!Среди функциональных способностей, можно также подчеркнуть «мультитач», функция, которая полностью перевернула мир сенсорных смартфонов! ',
                'price': 12000, 'old_price': 0,  'category': cat[0], 'qty': 0,   'producer': prod[0]},
               {'name': u'Apple iPhone 4s 64gb WiFi 3G + чехол в падарок', 'description': u'У данного Apple iPhone 4 32Gb, множество преимуществ, но самым явным, является новый ультрасовременный дисплей, повышенной четкости – Retina. Как и следовало ожидать, в данном Iphone, огромное количество функций, с которыми справится даже маленький ребенок!Именно на это и рассчитывал создатель компании Apple – Стив Джобс!Среди функциональных способностей, можно также подчеркнуть «мультитач», функция, которая полностью перевернула мир сенсорных смартфонов! ',
                'price': 16000, 'old_price': 0,  'category': cat[0], 'qty': 99,  'producer': prod[0]},
               {'name': u'Samsung Galaxy III 64gb полный фарш', 'description': u'У данного Apple iPhone 4 32Gb, множество преимуществ, но самым явным, является новый ультрасовременный дисплей, повышенной четкости – Retina. Как и следовало ожидать, в данном Iphone, огромное количество функций, с которыми справится даже маленький ребенок!Именно на это и рассчитывал создатель компании Apple – Стив Джобс!Среди функциональных способностей, можно также подчеркнуть «мультитач», функция, которая полностью перевернула мир сенсорных смартфонов! ',
                'price': 25000, 'old_price': 30000, 'category': cat[0], 'qty': 0,  'producer': prod[1]},
               {'name': u'Samsung Galaxy II 32gb', 'description': u'У данного Apple iPhone 4 32Gb, множество преимуществ, но самым явным, является новый ультрасовременный дисплей, повышенной четкости – Retina. Как и следовало ожидать, в данном Iphone, огромное количество функций, с которыми справится даже маленький ребенок!Именно на это и рассчитывал создатель компании Apple – Стив Джобс!Среди функциональных способностей, можно также подчеркнуть «мультитач», функция, которая полностью перевернула мир сенсорных смартфонов! ',
                'price': 24000, 'old_price': 0,  'category': cat[0], 'qty': 99,  'producer': prod[1]},
               {'name': u'Sumsung Galaxy Nexus', 'description': u'У данного Apple iPhone 4 32Gb, множество преимуществ, но самым явным, является новый ультрасовременный дисплей, повышенной четкости – Retina. Как и следовало ожидать, в данном Iphone, огромное количество функций, с которыми справится даже маленький ребенок!Именно на это и рассчитывал создатель компании Apple – Стив Джобс!Среди функциональных способностей, можно также подчеркнуть «мультитач», функция, которая полностью перевернула мир сенсорных смартфонов! ',
                'price': 12000, 'old_price': 0, 'category': cat[0], 'qty': 0,  'producer': prod[1]},
            )
            for p in products:
                p= Product.objects.create(
                    name=p['name'],
                    description=p['description'],
                    price=p['price'],
                    old_price=p['old_price'],
                    qty=p['qty'],
                    producer=p['producer'],
                    category=p['category']
                )
            get_status('Products', True)

def insert_product_img():
    try:
        p = ProductImage.objects.get(pk=1)
        get_status('ProductsImages', False)
    except ObjectDoesNotExist:
        products = Product.objects.all()
        for p in products:
            for i in range(5):
                r = str(random.randint(1,7))
                file_path = 'tmp/product'+r+'.jpg'
                i=ProductImage.objects.create(
                    product=p,
                    image =File(open(file_path)) ,
                )
        get_status('ProductsImages', True)

def upd_collections():
    coll=Collection.objects.all()
    for c in coll:
        c.products =Product.objects.order_by('?')[:3]
    print 'Updating Collections -- done'

def insert_pages():
    try:
        p = Page.objects.get(pk=1)
        get_status('Pages', False)
    except ObjectDoesNotExist:
        names = (
            u'Помощь',
            u'Оптовика',
            u'Контакты',
            )
        for n in names:
            p=Page.objects.create(
                name = n,
                short_name =n,
                description = u'Тестовое описание страницы',
                content = u'Текстовая старинца со своим каким то текстом, который отражает суть самой старицы. Например это может быть раздел помощи. В данном разделе будет информация о доставке, оплате и прочим вещам, которые помогут покупателю.',
                active = True,
            )
        p=Page.objects.create(
            name = u'Скрытая тестовая страница',
            short_name =u'Hiden page',
            description =u'Тестовое описание страницы',
            content = u'Текстовая старинца со своим каким то текстом, который отражает суть самой старицы. Например это может быть раздел помощи. В данном разделе будет информация о доставке, оплате и прочим вещам, которые помогут покупателю.',
            )
        get_status('Pages', True)

def insert_payment():
    try:
        p = PaymentMethod.objects.get(pk=1)
        get_status('PaymentMethods', False)
    except ObjectDoesNotExist:
        names = (
            u'Наличными курьеру',
            u'Электронными деньгами',
            u'Пластиковой картой',
            )
        for n in names:
            p=PaymentMethod.objects.create(
                name = n,
                description = u'Описание метода оплаты. Что это такое и как произести оплату, а так же сроки зачисления',
                active = True
            )
        get_status('PaymentMethods', True)


def insert_shipping():
    try:
        p = ShippingMethod.objects.get(pk=1)
        get_status('ShippingMethod', False)
    except ObjectDoesNotExist:
        names = (
            u'Доставка курьером (Москва, Обнинск)',
            u'Самовывоз',
            u'Доставка службой СПСР',
            )
        for n in names:
            p=ShippingMethod.objects.create(
                name = n,
                description = u'Описание способа доставки. Как это происходи и сколько занимает по времени. Плюсы и Минусы данной доставки',
                active = True,
                days = 3
            )
        p=ShippingMethod.objects.create(
            name = u'Доставка суппер героями',
            description =u'Ваш заказ может доставить суппер герой. Если надо быстро то суппермен или человек молния к вашим услугам. Хочется чего-то более пикантного, с нами работает женщина кошка',
            active = False,
            days = 0
        )
        get_status('ShippingMethod', True)


class Command(NoArgsCommand):
    def handle_noargs(self, *args, **options):
        print '\nInserting Shop tabels . . .\n ----------------------------------------------\n'
        insert_settings()
        insert_cat()
        insert_collections()
        insert_producer()
        insert_products()
        insert_product_img()
        upd_collections()
        insert_pages()
        insert_payment()
        insert_shipping()
        print '\n ----------------------------------------------\nShop tabels is ready\n'






