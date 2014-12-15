# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flatpages_placeholders', '0002_placeholder_visible'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placeholder',
            name='name',
            field=models.CharField(max_length=255, db_index=True),
        ),
        migrations.AlterUniqueTogether(
            name='placeholder',
            unique_together=set([('name', 'page')]),
        ),
    ]
