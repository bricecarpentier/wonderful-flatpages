from django.contrib.admin import ModelAdmin, site

from .models import Image


class ImageAdmin(ModelAdmin):
    pass

site.register(Image, ImageAdmin)
