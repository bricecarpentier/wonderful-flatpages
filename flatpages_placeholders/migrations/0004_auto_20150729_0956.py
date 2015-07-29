# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flatpages_placeholders', '0003_auto_20141215_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placeholder',
            name='content',
            field=models.TextField(blank=True, default=''),
        ),
    ]
