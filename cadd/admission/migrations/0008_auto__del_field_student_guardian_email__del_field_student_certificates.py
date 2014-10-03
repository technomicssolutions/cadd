# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Student.guardian_email'
        db.delete_column(u'admission_student', 'guardian_email')

        # Deleting field 'Student.certificates_file'
        db.delete_column(u'admission_student', 'certificates_file')

        # Deleting field 'Student.guardian_address'
        db.delete_column(u'admission_student', 'guardian_address')

        # Deleting field 'Student.land_number'
        db.delete_column(u'admission_student', 'land_number')

        # Deleting field 'Student.id_proofs_remarks'
        db.delete_column(u'admission_student', 'id_proofs_remarks')

        # Deleting field 'Student.certificates_remarks'
        db.delete_column(u'admission_student', 'certificates_remarks')

        # Deleting field 'Student.guardian_land_number'
        db.delete_column(u'admission_student', 'guardian_land_number')

        # Deleting field 'Student.id_proofs_file'
        db.delete_column(u'admission_student', 'id_proofs_file')

        # Adding field 'Student.unique_id'
        db.add_column(u'admission_student', 'unique_id',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Student.cadd_registration_no'
        db.add_column(u'admission_student', 'cadd_registration_no',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Student.qualifications'
        db.add_column(u'admission_student', 'qualifications',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


        # Changing field 'Student.roll_number'
        db.alter_column(u'admission_student', 'roll_number', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))
    def backwards(self, orm):
        # Adding field 'Student.guardian_email'
        db.add_column(u'admission_student', 'guardian_email',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Student.certificates_file'
        db.add_column(u'admission_student', 'certificates_file',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Student.guardian_address'
        db.add_column(u'admission_student', 'guardian_address',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Student.land_number'
        db.add_column(u'admission_student', 'land_number',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Student.id_proofs_remarks'
        db.add_column(u'admission_student', 'id_proofs_remarks',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Student.certificates_remarks'
        db.add_column(u'admission_student', 'certificates_remarks',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Student.guardian_land_number'
        db.add_column(u'admission_student', 'guardian_land_number',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Student.id_proofs_file'
        db.add_column(u'admission_student', 'id_proofs_file',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Student.unique_id'
        db.delete_column(u'admission_student', 'unique_id')

        # Deleting field 'Student.cadd_registration_no'
        db.delete_column(u'admission_student', 'cadd_registration_no')

        # Deleting field 'Student.qualifications'
        db.delete_column(u'admission_student', 'qualifications')


        # Changing field 'Student.roll_number'
        db.alter_column(u'admission_student', 'roll_number', self.gf('django.db.models.fields.IntegerField')(null=True))
    models = {
        u'admission.enquiry': {
            'Meta': {'object_name': 'Enquiry'},
            'address': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'auto_generated_num': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['college.Course']", 'null': 'True', 'blank': 'True'}),
            'details_about_clients_enquiry': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'discount': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'educational_qualification': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'follow_up_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'land_mark': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'mobile_number': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'remarks': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'remarks_for_follow_up_date': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'student_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'admission.student': {
            'Meta': {'object_name': 'Student'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'batch': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['college.Batch']", 'null': 'True', 'blank': 'True'}),
            'blood_group': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'cadd_registration_no': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'certificates_submitted': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['college.Course']", 'null': 'True', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'doj': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'guardian_mobile_number': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'guardian_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_proofs_submitted': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'is_rolled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mobile_number': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'qualifications': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'relationship': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'roll_number': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'student_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'unique_id': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'college.batch': {
            'Meta': {'object_name': 'Batch'},
            'allowed_students': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'end_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'no_of_students': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'software': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['college.Software']"}),
            'start_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'college.course': {
            'Meta': {'object_name': 'Course'},
            'amount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'duration': ('django.db.models.fields.IntegerField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'duration_unit': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'fine': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'software': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['college.Software']", 'symmetrical': 'False'})
        },
        u'college.software': {
            'Meta': {'object_name': 'Software'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['admission']