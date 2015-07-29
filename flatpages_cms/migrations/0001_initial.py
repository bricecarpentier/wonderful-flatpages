# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=255, verbose_name='name', default='', blank=True)),
                ('description', models.TextField(verbose_name='description', default='', blank=True)),
                ('alternative_text', models.CharField(max_length=255, verbose_name='alternative text', default='', blank=True)),
                ('file', models.ImageField(upload_to='images/', verbose_name='file', height_field='height', width_field='width')),
                ('width', models.FloatField(verbose_name='width', null=True, blank=True)),
                ('height', models.FloatField(verbose_name='height', null=True, blank=True)),
            ],
        ),
    ]
