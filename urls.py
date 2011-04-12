from django.conf.urls.defaults import *
from django.conf import settings
from mibooklist.views import index, search, sort, advanced_search, delete_user
from mibooklist.sellers.views import profile, books
from sellers.forms import SupportForm, ContactSellerForm
from contact_form.views import contact_form
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^mibooklist/', include('mibooklist.foo.urls')),
    (r'^$', index),
    (r'^search/$', search),
    (r'^advanced_search/$', advanced_search),
    (r'^sort/$', sort),
    (r'^books/', include('books.urls')),
    (r'^accounts/profile/$', profile),
    (r'^accounts/books/$', books),
    (r'^accounts/delete/(?P<id>\d+)/$', delete_user),
    (r'^accounts/', include('registration.backends.default.urls')),
    (r'^profiles/', include('profiles.urls')),
    url(r'^contact-seller/$',contact_form, {'form_class': ContactSellerForm,'success_url': '/contact-seller/sent/'}, name='contact_seller',),
    url(r'^contact-seller/sent/$',direct_to_template,{ 'template': 'contact_form/seller_form_sent.html' }, name='seller_form_sent'),
    url(r'^support/$',contact_form, {'form_class': SupportForm}, name='contact_form',),
    url(r'^support/sent/$',direct_to_template,{ 'template': 'contact_form/contact_form_sent.html' }, name='contact_form_sent'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/templatesadmin/', include('templatesadmin.urls')),
    (r'^admin/photologue', include('photologue.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^grappelli/', include('grappelli.urls')),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
