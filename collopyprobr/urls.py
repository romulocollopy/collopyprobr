from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('collopyprobr.core.views',
        url(r'^$', 'homepage', name='home'),
        url(r'^posts/(?P<id>[0-9]+)$', 'postdetail', name='detail'),
        url(r'^posts/', 'postslist', name='post'),
        url(r'^about/$', 'aboutpage', name='about'),
        url(r'^contact/$', 'contactpage', name='contact'),
        url(r'^admin/', include(admin.site.urls)),
        )
