from django.conf.urls import url

from .views import CreateImageView


urlpatterns = [
    url(r'^create/$', CreateImageView.as_view(), name='image-create'),
]
