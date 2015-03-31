# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Placeholder'
        db.create_table(u'flatpages_placeholders_placeholder', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
            ('page', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['flatpages.FlatPage'], null=True)),
            ('content', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('visible', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'flatpages_placeholders', ['Placeholder'])

        # Adding unique constraint on 'Placeholder', fields ['name', 'page']
        db.create_unique(u'flatpages_placeholders_placeholder', ['name', 'page_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Placeholder', fields ['name', 'page']
        db.delete_unique(u'flatpages_placeholders_placeholder', ['name', 'page_id'])

        # Deleting model 'Placeholder'
        db.delete_table(u'flatpages_placeholders_placeholder')


    models = {
        u'flatpages.flatpage': {
            'Meta': {'ordering': "(u'url',)", 'object_name': 'FlatPage', 'db_table': "u'django_flatpage'"},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enable_comments': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'registration_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['sites.Site']", 'symmetrical': 'False'}),
            'template_name': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'})
        },
        u'flatpages_placeholders.placeholder': {
            'Meta': {'unique_together': "[('name', 'page')]", 'object_name': 'Placeholder'},
            'content': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['flatpages.FlatPage']", 'null': 'True'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['flatpages_placeholders']