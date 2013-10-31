from django.conf.urls.defaults import patterns, url
from django.conf.urls.defaults import include
from rest_framework.urlpatterns import format_suffix_patterns
from events import views

urlpatterns = patterns('',

    url(r'^events$', views.EventList.as_view()),
    url(r'^events/new$', views.EventNew.as_view()),
    url(r'^events/(?P<pk>[0-9]+)$', views.EventDetail.as_view()),

    #Authentication by browser
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

)

urlpatterns = format_suffix_patterns(urlpatterns)
