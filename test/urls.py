from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

import altas.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gettingstarted.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^$', altas.views.index, name='index'),
    url(r'^db', altas.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^test/', altas.views.test, name='test'),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),
    
    url(r'^$','altas.views.inicio'),
    url(r'^registro/$','altas.views.registro'),
    url(r'^contrasena/$','altas.views.contrasena'),
    url(r'^contacto/$','altas.views.contacto'),
    url(r'^generar_usuarios/$','altas.views.generar_script'),
)
