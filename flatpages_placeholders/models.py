from django.contrib.flatpages.models import FlatPage
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Placeholder(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    page = models.ForeignKey(FlatPage, null=True, db_index=True)
    content = models.TextField(blank=True, default='')
    visible = models.BooleanField(default=False)

    def __str__(self):
        return '{}|{}'.format(self.page_id if self.page_id else '', self.name)

    class Meta:
        unique_together = [('name', 'page'), ]
