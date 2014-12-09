from django.contrib.admin import ModelAdmin, register

from .models import Placeholder


@register(Placeholder)
class PlaceholderAdmin(ModelAdmin):
    list_display = ('name', 'page', )
    list_filter = ('page', )
    search_fields = ('name', )
