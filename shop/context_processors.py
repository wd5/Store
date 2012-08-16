# -*- coding: utf-8 -*-

from shop.models import Settings
from django.core.exceptions import ObjectDoesNotExist

def settings(request):
    try:
        settings = Settings.objects.get(active=True)
    except ObjectDoesNotExist:
        settings = {}
    return { 'settings': settings, }
