# -*- coding: utf-8 -*-
from django.db import models
from sorl.thumbnail.shortcuts import get_thumbnail

class Banner(models.Model):
    LOCATION = (
        ('home_offers', 'На главной'),
        )
    title = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=40, blank=True, null=True)
    image = models.ImageField(upload_to='banners')
    url = models.URLField(max_length=100)
    location = models.CharField(max_length=20, default='home_offers', choices=LOCATION)
    active = models.BooleanField(default=False)
    position = models.PositiveIntegerField(default=999)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["position"]

    def get_thumbnail(self, width,  height):
        img = self.image
        return unicode(get_thumbnail(img, '%ix%i' % (width,  height)).url)