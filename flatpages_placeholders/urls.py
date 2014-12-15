from django.conf.urls import patterns, url

from .views import PlaceholderUpdateView


urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)$', PlaceholderUpdateView.as_view(), name='placeholder_update'),
)
