# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flatpages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Placeholder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, db_index=True)),
                ('content', models.TextField(default=b'', blank=True)),
                ('page', models.ForeignKey(to='flatpages.FlatPage', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
