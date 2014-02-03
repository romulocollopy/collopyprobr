from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('collopyprobr.core.views',
        url(r'^$', 'homepage', name='home'),
        url(r'^about/', 'about', name='about'),
        url(r'^contact/', 'contact', name='contact'), 
        url(r'^admin/', include(admin.site.urls)),
        )
