from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from collopyprobr.core.views import HomeView

urlpatterns = patterns('',
        url(r'^$', HomeView.as_view(),name='home'),
        # url(r'^blog/', include('blog.urls')),
        url(r'^admin/', include(admin.site.urls)),
)
