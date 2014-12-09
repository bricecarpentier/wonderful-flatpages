# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flatpages_placeholders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='placeholder',
            name='visible',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
