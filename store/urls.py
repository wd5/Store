# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
from shop.views import home

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'storly.views.home', name='home'),
    # url(r'^storly/', include('storly.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home),
    url(r'^catalog/$', home),
    #url(r'^category/(?P<slug>[^/]+)/$', 'category'),
    #url(r'^product/(?P<slug>[^/]+)/$', 'category'),
)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^(?P<path>.+)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
