# -*- coding: utf-8 -*-

import sys
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import NoArgsCommand
from django.core.files import File
import random

from banners.models import *

def get_status(name, status):
    if status:
        status = 'done'
    else:
        status = 'already exists '
    print 'Inserting '+name+ ' -- ' +status

def insert_banners():
    try:
        banners = Banner.objects.get(pk=1)
        get_status('Banners', False)
    except ObjectDoesNotExist:
        titles = (
            u'Телефоны',
            u'Планшеты',
            u'Оптовые поставки',
            )
        i=1
        for t in titles:
            file_path = 'tmp/banner'+str(i)+'.jpg'
            b = Banner.objects.create(
                title =t,
                description = u'баннер на главной',
                image =File(open(file_path)),
                location = u'home_offers',
                url = u'/catalog/',
                active = True,
                position = i,
            )
            i+=1
        get_status('Banners', True)

class Command(NoArgsCommand):
    def handle_noargs(self, *args, **options):
        print '\nInserting Banners tabels . . .\n ----------------------------------------------\n'
        insert_banners()
        print '\n ----------------------------------------------\nBanners tabels is ready\n'