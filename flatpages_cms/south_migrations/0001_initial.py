# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Image'
        db.create_table(u'flatpages_cms_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('alternative_text', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
            ('file', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('width', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'flatpages_cms', ['Image'])


    def backwards(self, orm):
        # Deleting model 'Image'
        db.delete_table(u'flatpages_cms_image')


    models = {
        u'flatpages_cms.image': {
            'Meta': {'object_name': 'Image'},
            'alternative_text': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'height': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'width': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['flatpages_cms']