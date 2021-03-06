from django.conf.urls import patterns, include, url
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
from django.views.generic import TemplateView
from django.conf import settings
dajaxice_autodiscover()

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'dataminas.views.home', name='home'),
    url(r'^sobre/$', TemplateView.as_view(template_name='dataminas/about.html'), name='about'),
    url(r'^dados/(?P<category>[a-z\-]+)/$', 'dataminas.views.show_category', name='show_category'),
    url(r'^dados/(?P<category>[a-z\-]+)/(?P<subcategory>[a-z\-]+)/$', 'dataminas.views.show_subcategory', name='show_subcategory'),
    url(r'^ponto/(?P<pk>[0-9]+)/$', 'dataminas.views.show_point', name='show_point'),
)
