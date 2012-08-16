# -*- coding: utf-8 -*-

import sys
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import NoArgsCommand
from django.core.files import File
import random

from slider.models import *

def get_status(name, status):
    if status:
        status = 'done'
    else:
        status = 'already exists '
    print 'Inserting '+name+ ' -- ' +status

def insert_slider():
    try:
        slide = Slider.objects.get(pk=1)
        get_status('Slides', False)
    except ObjectDoesNotExist:
        titles = (
            u'iPhone по суппер цене',
            u'Горячее предложение на iPad',
            )
        i=1
        for t in titles:
            file_path = 'tmp/slide'+str(i)+'.jpg'
            s = Slider.objects.create(
                title =t,
                description = u'Описание предложения',
                image =File(open(file_path)),
                url = u'/catalog/',
                active = True,
                position = i,
            )
            i+=1
        get_status('Slides', True)

class Command(NoArgsCommand):
    def handle_noargs(self, *args, **options):
        print '\nInserting Slider tabels . . .\n ----------------------------------------------\n'
        insert_slider()
        print '\n ----------------------------------------------\nSlider  tabels is ready\n'