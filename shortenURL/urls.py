from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shortenURL.views.home', name='home'),
    # url(r'^shortenURL/', include('shortenURL.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATICFILES_DIRS[0]}),

    url(r'^$', 'shortenURL.magic.views.welcome', name='welcome'),
    url(r'^short/$', 'shortenURL.magic.views.short', name='short'),
    url(r'^(?P<shortenURL>.*)$', 'shortenURL.magic.views.recover')
)
