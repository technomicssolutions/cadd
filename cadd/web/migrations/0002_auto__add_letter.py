# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Letter'
        db.create_table(u'web_letter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('letter_type', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('to_address', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('from_address', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'web', ['Letter'])

    def backwards(self, orm):
        # Deleting model 'Letter'
        db.delete_table(u'web_letter')

    models = {
        u'web.letter': {
            'Meta': {'object_name': 'Letter'},
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'from_address': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'letter_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'to_address': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['web']