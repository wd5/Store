# -*- coding: utf-8 -*-

from django.template import TemplateDoesNotExist
from django.views.generic.simple import direct_to_template
from slider.models import *
from banners.models import *
from shop.models import *
from django.template import Context
from django.core.exceptions import ObjectDoesNotExist

def home(request):
    try:
        slider = Slider.objects.filter(active=True)
        for slide in slider:
            slide.image = slide.get_thumbnail(940, 380)
    except ObjectDoesNotExist:
        slider = {}
    try:
        banners = Banner.objects.filter(location = 'home_offers')
        banners =banners.filter(active = True)[:3]
        for banner in banners:
            banner.image = banner.get_thumbnail(300, 167)
    except ObjectDoesNotExist:
        slider = {}
    context = {
        'slider':slider,
        'banners':banners,
        }
    return direct_to_template(request, 'home.html', context)

def catalog(request):
    try:
        categories = Category.objects.filter(active=True)
    except ObjectDoesNotExist:
        categories = {}

