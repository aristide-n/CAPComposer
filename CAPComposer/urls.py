from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^$', 'CAPComposer.views.alert'),
    url(r'^alert', 'CAPComposer.views.alert'),
    url(r'^map', 'CAPComposer.views.map'),
    url(r'^info', 'CAPComposer.views.info'),
    url(r'^finish', 'CAPComposer.views.finish'),
)

urlpatterns += staticfiles_urlpatterns()