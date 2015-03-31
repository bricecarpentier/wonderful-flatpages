from django.contrib.admin import ModelAdmin, site

from .models import Placeholder


class PlaceholderAdmin(ModelAdmin):
    list_display = ('name', 'page', 'visible', )
    list_filter = ('page', )
    search_fields = ('name', )

site.register(Placeholder, PlaceholderAdmin)
