from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Image(models.Model):
    name = models.CharField(_('name'),
        max_length=255,
        blank=True, default='')
    description = models.TextField(_('description'),
        blank=True, default='')
    alternative_text = models.CharField(_('alternative text'),
        max_length=255,
        blank=True, default='')

    file = models.ImageField(_('file'),
        upload_to='images/',
        width_field='width',
        height_field='height')
    width = models.FloatField(_('width'),
        blank=True, null=True)
    height = models.FloatField(_('height'),
        blank=True, null=True)

    def __str__(self):
        return self.name or self.file.name
