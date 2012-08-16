# -*- coding: utf-8 -*-
from django.db import models

from sorl.thumbnail.shortcuts import get_thumbnail

class Slider(models.Model):
    title = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=40, blank=True, null=True)
    image = models.ImageField(upload_to='slides')
    active = models.BooleanField(default=False)
    url = models.URLField(max_length=100)
    position = models.PositiveSmallIntegerField(default=999)

    def __unicode__(self):
        return self.title

    def get_thumbnail(self, width,  height):
        img = self.image
        return unicode(get_thumbnail(img, '%ix%i' % (width,  height)).url)