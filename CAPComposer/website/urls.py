from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'website.views.alert'),
    url(r'^alert', 'website.views.alert'),
    url(r'^map', 'website.views.map'),
    url(r'^info', 'website.views.info'),
    url(r'^finish', 'website.views.finish'),
    )
