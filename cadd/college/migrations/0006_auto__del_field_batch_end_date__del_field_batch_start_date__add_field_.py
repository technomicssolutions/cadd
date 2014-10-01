# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Batch.end_date'
        db.delete_column(u'college_batch', 'end_date')

        # Deleting field 'Batch.start_date'
        db.delete_column(u'college_batch', 'start_date')

        # Adding field 'Batch.start_time'
        db.add_column(u'college_batch', 'start_time',
                      self.gf('django.db.models.fields.TimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Batch.end_time'
        db.add_column(u'college_batch', 'end_time',
                      self.gf('django.db.models.fields.TimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Batch.allowed_students'
        db.add_column(u'college_batch', 'allowed_students',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

    def backwards(self, orm):
        # Adding field 'Batch.end_date'
        db.add_column(u'college_batch', 'end_date',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Batch.start_date'
        db.add_column(u'college_batch', 'start_date',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Batch.start_time'
        db.delete_column(u'college_batch', 'start_time')

        # Deleting field 'Batch.end_time'
        db.delete_column(u'college_batch', 'end_time')

        # Deleting field 'Batch.allowed_students'
        db.delete_column(u'college_batch', 'allowed_students')

    models = {
        u'college.batch': {
            'Meta': {'object_name': 'Batch'},
            'allowed_students': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'end_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no_of_students': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'software': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['college.Software']"}),
            'start_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'college.course': {
            'Meta': {'object_name': 'Course'},
            'amount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'duration': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'software': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['college.Software']", 'symmetrical': 'False'})
        },
        u'college.software': {
            'Meta': {'object_name': 'Software'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['college']