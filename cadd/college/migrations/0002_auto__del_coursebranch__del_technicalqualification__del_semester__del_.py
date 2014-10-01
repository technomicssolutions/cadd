# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'CourseBranch'
        db.delete_table(u'college_coursebranch')

        # Deleting model 'TechnicalQualification'
        db.delete_table(u'college_technicalqualification')

        # Deleting model 'Semester'
        db.delete_table(u'college_semester')

        # Deleting model 'QualifiedExam'
        db.delete_table(u'college_qualifiedexam')

        # Deleting model 'College'
        db.delete_table(u'college_college')

        # Deleting model 'Branch'
        db.delete_table(u'college_branch')

        # Adding model 'Software'
        db.create_table(u'college_software', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'college', ['Software'])

        # Deleting field 'Course.course'
        db.delete_column(u'college_course', 'course')

        # Adding field 'Course.name'
        db.add_column(u'college_course', 'name',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Course.amount'
        db.add_column(u'college_course', 'amount',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True),
                      keep_default=False)

        # Adding field 'Course.duration'
        db.add_column(u'college_course', 'duration',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Removing M2M table for field semester on 'Course'
        db.delete_table('college_course_semester')

        # Adding M2M table for field software on 'Course'
        db.create_table(u'college_course_software', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('course', models.ForeignKey(orm[u'college.course'], null=False)),
            ('software', models.ForeignKey(orm[u'college.software'], null=False))
        ))
        db.create_unique(u'college_course_software', ['course_id', 'software_id'])

        # Deleting field 'Batch.course'
        db.delete_column(u'college_batch', 'course_id')

        # Deleting field 'Batch.periods'
        db.delete_column(u'college_batch', 'periods')

        # Deleting field 'Batch.branch'
        db.delete_column(u'college_batch', 'branch_id')

        # Adding field 'Batch.software'
        db.add_column(u'college_batch', 'software',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['college.Software']),
                      keep_default=False)

        # Adding field 'Batch.no_of_students'
        db.add_column(u'college_batch', 'no_of_students',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


        # Changing field 'Batch.start_date'
        db.alter_column(u'college_batch', 'start_date', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Batch.end_date'
        db.alter_column(u'college_batch', 'end_date', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))
    def backwards(self, orm):
        # Adding model 'CourseBranch'
        db.create_table(u'college_coursebranch', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('branch', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'college', ['CourseBranch'])

        # Adding model 'TechnicalQualification'
        db.create_table(u'college_technicalqualification', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('authority', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
        ))
        db.send_create_signal(u'college', ['TechnicalQualification'])

        # Adding model 'Semester'
        db.create_table(u'college_semester', (
            ('semester', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'college', ['Semester'])

        # Adding model 'QualifiedExam'
        db.create_table(u'college_qualifiedexam', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('authority', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'college', ['QualifiedExam'])

        # Adding model 'College'
        db.create_table(u'college_college', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('registration_number', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'college', ['College'])

        # Adding model 'Branch'
        db.create_table(u'college_branch', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('branch', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'college', ['Branch'])

        # Deleting model 'Software'
        db.delete_table(u'college_software')

        # Adding field 'Course.course'
        db.add_column(u'college_course', 'course',
                      self.gf('django.db.models.fields.CharField')(unique=True, max_length=200, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Course.name'
        db.delete_column(u'college_course', 'name')

        # Deleting field 'Course.amount'
        db.delete_column(u'college_course', 'amount')

        # Deleting field 'Course.duration'
        db.delete_column(u'college_course', 'duration')

        # Adding M2M table for field semester on 'Course'
        db.create_table(u'college_course_semester', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('course', models.ForeignKey(orm[u'college.course'], null=False)),
            ('semester', models.ForeignKey(orm[u'college.semester'], null=False))
        ))
        db.create_unique(u'college_course_semester', ['course_id', 'semester_id'])

        # Removing M2M table for field software on 'Course'
        db.delete_table('college_course_software')

        # Adding field 'Batch.course'
        db.add_column(u'college_batch', 'course',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['college.Course'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Batch.periods'
        db.add_column(u'college_batch', 'periods',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Batch.branch'
        db.add_column(u'college_batch', 'branch',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['college.CourseBranch'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Batch.software'
        db.delete_column(u'college_batch', 'software_id')

        # Deleting field 'Batch.no_of_students'
        db.delete_column(u'college_batch', 'no_of_students')


        # Changing field 'Batch.start_date'
        db.alter_column(u'college_batch', 'start_date', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Batch.end_date'
        db.alter_column(u'college_batch', 'end_date', self.gf('django.db.models.fields.IntegerField')(null=True))
    models = {
        u'college.batch': {
            'Meta': {'object_name': 'Batch'},
            'end_date': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no_of_students': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'software': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['college.Software']"}),
            'start_date': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['college']