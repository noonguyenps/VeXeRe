from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from welcome.views import index, health

urlpatterns = [
    url(r'^$', index),
    url(r'^health$', health),
    url(r'^admin/', include(admin.site.urls)),
    path('', include('customers.urls')),
    path('manager', include('managers.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
