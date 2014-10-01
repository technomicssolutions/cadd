# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Designation'
        db.delete_table(u'staff_designation')

        # Adding model 'Permission'
        db.create_table(u'staff_permission', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('attendance_module', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('admission_module', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('college_module', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('fees_module', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'staff', ['Permission'])

        # Deleting field 'Staff.guardian_email'
        db.delete_column(u'staff_staff', 'guardian_email')

        # Deleting field 'Staff.staff_id'
        db.delete_column(u'staff_staff', 'staff_id')

        # Deleting field 'Staff.reference_land_number'
        db.delete_column(u'staff_staff', 'reference_land_number')

        # Deleting field 'Staff.guardian_land_number'
        db.delete_column(u'staff_staff', 'guardian_land_number')

        # Deleting field 'Staff.designation'
        db.delete_column(u'staff_staff', 'designation_id')

        # Deleting field 'Staff.reference_email'
        db.delete_column(u'staff_staff', 'reference_email')

        # Adding field 'Staff.permission'
        db.add_column(u'staff_staff', 'permission',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['staff.Permission'], null=True, blank=True),
                      keep_default=False)


        # Changing field 'Staff.reference_address'
        db.alter_column(u'staff_staff', 'reference_address', self.gf('django.db.models.fields.TextField')(max_length=200, null=True))

        # Changing field 'Staff.id_proofs_submitted'
        db.alter_column(u'staff_staff', 'id_proofs_submitted', self.gf('django.db.models.fields.TextField')(max_length=200, null=True))

        # Changing field 'Staff.guardian_address'
        db.alter_column(u'staff_staff', 'guardian_address', self.gf('django.db.models.fields.TextField')(max_length=200, null=True))

        # Changing field 'Staff.id_proofs_remarks'
        db.alter_column(u'staff_staff', 'id_proofs_remarks', self.gf('django.db.models.fields.TextField')(max_length=200, null=True))

        # Changing field 'Staff.qualifications'
        db.alter_column(u'staff_staff', 'qualifications', self.gf('django.db.models.fields.TextField')(max_length=200, null=True))

        # Changing field 'Staff.certificates_remarks'
        db.alter_column(u'staff_staff', 'certificates_remarks', self.gf('django.db.models.fields.TextField')(max_length=200, null=True))

        # Changing field 'Staff.certificates_submitted'
        db.alter_column(u'staff_staff', 'certificates_submitted', self.gf('django.db.models.fields.TextField')(max_length=200, null=True))

        # Changing field 'Staff.address'
        db.alter_column(u'staff_staff', 'address', self.gf('django.db.models.fields.TextField')(max_length=200, null=True))
    def backwards(self, orm):
        # Adding model 'Designation'
        db.create_table(u'staff_designation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('designation', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'staff', ['Designation'])

        # Deleting model 'Permission'
        db.delete_table(u'staff_permission')

        # Adding field 'Staff.guardian_email'
        db.add_column(u'staff_staff', 'guardian_email',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Staff.staff_id'
        raise RuntimeError("Cannot reverse this migration. 'Staff.staff_id' and its values cannot be restored.")
        # Adding field 'Staff.reference_land_number'
        db.add_column(u'staff_staff', 'reference_land_number',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Staff.guardian_land_number'
        db.add_column(u'staff_staff', 'guardian_land_number',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Staff.designation'
        db.add_column(u'staff_staff', 'designation',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['staff.Designation'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Staff.reference_email'
        db.add_column(u'staff_staff', 'reference_email',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Staff.permission'
        db.delete_column(u'staff_staff', 'permission_id')


        # Changing field 'Staff.reference_address'
        db.alter_column(u'staff_staff', 'reference_address', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Staff.id_proofs_submitted'
        db.alter_column(u'staff_staff', 'id_proofs_submitted', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Staff.guardian_address'
        db.alter_column(u'staff_staff', 'guardian_address', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Staff.id_proofs_remarks'
        db.alter_column(u'staff_staff', 'id_proofs_remarks', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Staff.qualifications'
        db.alter_column(u'staff_staff', 'qualifications', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Staff.certificates_remarks'
        db.alter_column(u'staff_staff', 'certificates_remarks', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Staff.certificates_submitted'
        db.alter_column(u'staff_staff', 'certificates_submitted', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Staff.address'
        db.alter_column(u'staff_staff', 'address', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))
    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'staff.permission': {
            'Meta': {'object_name': 'Permission'},
            'admission_module': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'attendance_module': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'college_module': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fees_module': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'staff.staff': {
            'Meta': {'object_name': 'Staff'},
            'address': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'blood_group': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'certificates_file': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'certificates_remarks': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'certificates_submitted': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'doj': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'experiance': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'guardian_address': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'guardian_mobile_number': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'guardian_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_proofs_file': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id_proofs_remarks': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id_proofs_submitted': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'land_number': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'mobile_number': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'permission': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['staff.Permission']", 'null': 'True', 'blank': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'qualifications': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'reference_address': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'reference_mobile_number': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'reference_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'relationship': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['staff']