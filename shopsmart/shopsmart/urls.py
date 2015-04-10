
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', 'home.views.landing', name='landing'),
                       url(r'^home/$', 'home.views.index', name='index'),
                       url(r'^products/$', 'home.views.products', name='products'),
                       url(r'^email/$', 'home.views.email', name='email'),
                       url(r'^price_check/$', 'home.views.price_check', name='price_check'),
                       url(r'^add_stuff/$', 'home.views.add_stuff', name='add_stuff'),

    url(r'^admin/', include(admin.site.urls)),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
