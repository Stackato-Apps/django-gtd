from django.conf.urls.defaults import *
from django.contrib import admin
from django.contrib import databrowse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^databrowse/(.*)', login_required(databrowse.site.root)),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^gtd/', include('gtd.urls')),
    url(r'^$', lambda request: redirect('/gtd')),
)

if settings.DEBUG or settings.STACKATO:
    from os.path import join, dirname, abspath
    urlpatterns += patterns('',
        url(r'^media/admin/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': abspath(join(dirname(admin.__file__), 'media')), 'show_indexes': True}),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
)
