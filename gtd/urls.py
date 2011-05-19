from django.conf.urls.defaults import *

urlpatterns = patterns('gtd.views',
    url(r'^$',                      'dashboard.dashboard',      name='dashboard'),
    url(r'^thing/$',                'objects.thing_list',       name='thing_list'),
    url(r'^thing/(?P<id>\d+)$',     'objects.thing_detail',     name='thing_detail'),     
    url(r'^context/$',              'objects.context_list',     name='context_list'),
    url(r'^context/(?P<id>\d+)$',   'objects.context_detail',   name='context_detail'), 
    url(r'^project/$',              'objects.project_list',     name='project_list'),
    url(r'^project/(?P<id>\d+)$',   'objects.project_detail',   name='project_detail'),
)
