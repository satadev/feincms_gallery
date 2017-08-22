try:
    from django.conf.urls import url
except ImportError:  # Older Django versions
    from django.conf.urls.defaults import url

from gallery.admin import admin_thumbnail


if django.VERSION[:2] >= (1, 10):
    urlpatterns = [
        url(r'^thumbnail/$', admin_thumbnail, name='gallery_admin_thumbnail'),
    ]
else:
    urlpatterns = patterns('',
        url(r'^thumbnail/$', admin_thumbnail, name='gallery_admin_thumbnail'),
    )
