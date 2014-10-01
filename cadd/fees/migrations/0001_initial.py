# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Installment'
        db.create_table(u'fees_installment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('due_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('amount', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=14, decimal_places=2)),
            ('fine_amount', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=14, decimal_places=2)),
        ))
        db.send_create_signal(u'fees', ['Installment'])

        # Adding model 'FeesHead'
        db.create_table(u'fees_feeshead', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('amount', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=14, decimal_places=2)),
        ))
        db.send_create_signal(u'fees', ['FeesHead'])

        # Adding model 'FeesStructureHead'
        db.create_table(u'fees_feesstructurehead', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('amount', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=14, decimal_places=2)),
            ('no_installments', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'fees', ['FeesStructureHead'])

        # Adding M2M table for field installments on 'FeesStructureHead'
        db.create_table(u'fees_feesstructurehead_installments', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('feesstructurehead', models.ForeignKey(orm[u'fees.feesstructurehead'], null=False)),
            ('installment', models.ForeignKey(orm[u'fees.installment'], null=False))
        ))
        db.create_unique(u'fees_feesstructurehead_installments', ['feesstructurehead_id', 'installment_id'])

        # Adding model 'FeesStructure'
        db.create_table(u'fees_feesstructure', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['college.Course'], null=True, blank=True)),
            ('batch', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['college.Batch'], null=True, blank=True)),
        ))
        db.send_create_signal(u'fees', ['FeesStructure'])

        # Adding M2M table for field head on 'FeesStructure'
        db.create_table(u'fees_feesstructure_head', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('feesstructure', models.ForeignKey(orm[u'fees.feesstructure'], null=False)),
            ('feesstructurehead', models.ForeignKey(orm[u'fees.feesstructurehead'], null=False))
        ))
        db.create_unique(u'fees_feesstructure_head', ['feesstructure_id', 'feesstructurehead_id'])

        # Adding model 'FeesPaymentInstallment'
        db.create_table(u'fees_feespaymentinstallment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['admission.Student'], null=True, blank=True)),
            ('total_amount', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=14, decimal_places=2)),
            ('installment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fees.Installment'], null=True, blank=True)),
            ('paid_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('paid_amount', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=14, decimal_places=2)),
            ('installment_amount', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=14, decimal_places=2)),
            ('installment_fine', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=14, decimal_places=2)),
        ))
        db.send_create_signal(u'fees', ['FeesPaymentInstallment'])

        # Adding model 'FeesPayment'
        db.create_table(u'fees_feespayment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fee_structure', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fees.FeesStructure'], null=True, blank=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['admission.Student'], null=True, blank=True)),
        ))
        db.send_create_signal(u'fees', ['FeesPayment'])

        # Adding M2M table for field payment_installment on 'FeesPayment'
        db.create_table(u'fees_feespayment_payment_installment', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('feespayment', models.ForeignKey(orm[u'fees.feespayment'], null=False)),
            ('feespaymentinstallment', models.ForeignKey(orm[u'fees.feespaymentinstallment'], null=False))
        ))
        db.create_unique(u'fees_feespayment_payment_installment', ['feespayment_id', 'feespaymentinstallment_id'])

        # Adding model 'CommonFeesPayment'
        db.create_table(u'fees_commonfeespayment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['admission.Student'], null=True, blank=True)),
            ('head', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fees.FeesHead'], null=True, blank=True)),
            ('paid_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('paid_amount', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=14, decimal_places=2)),
        ))
        db.send_create_signal(u'fees', ['CommonFeesPayment'])

    def backwards(self, orm):
        # Deleting model 'Installment'
        db.delete_table(u'fees_installment')

        # Deleting model 'FeesHead'
        db.delete_table(u'fees_feeshead')

        # Deleting model 'FeesStructureHead'
        db.delete_table(u'fees_feesstructurehead')

        # Removing M2M table for field installments on 'FeesStructureHead'
        db.delete_table('fees_feesstructurehead_installments')

        # Deleting model 'FeesStructure'
        db.delete_table(u'fees_feesstructure')

        # Removing M2M table for field head on 'FeesStructure'
        db.delete_table('fees_feesstructure_head')

        # Deleting model 'FeesPaymentInstallment'
        db.delete_table(u'fees_feespaymentinstallment')

        # Deleting model 'FeesPayment'
        db.delete_table(u'fees_feespayment')

        # Removing M2M table for field payment_installment on 'FeesPayment'
        db.delete_table('fees_feespayment_payment_installment')

        # Deleting model 'CommonFeesPayment'
        db.delete_table(u'fees_commonfeespayment')

    models = {
        u'admission.student': {
            'Meta': {'object_name': 'Student'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'batch': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['college.Batch']", 'null': 'True', 'blank': 'True'}),
            'blood_group': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'certificates_file': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'certificates_remarks': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'certificates_submitted': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['college.Course']", 'null': 'True', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'doj': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'guardian_address': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'guardian_email': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'guardian_land_number': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'guardian_mobile_number': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'guardian_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_proofs_file': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id_proofs_remarks': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id_proofs_submitted': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'land_number': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'mobile_number': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'qualified_exam': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['college.QualifiedExam']", 'null': 'True', 'blank': 'True'}),
            'relationship': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'roll_number': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'student_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'technical_qualification': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['college.TechnicalQualification']", 'null': 'True', 'blank': 'True'})
        },
        u'college.batch': {
            'Meta': {'object_name': 'Batch'},
            'branch': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['college.CourseBranch']", 'null': 'True', 'blank': 'True'}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['college.Course']", 'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'periods': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'college.course': {
            'Meta': {'object_name': 'Course'},
            'course': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'semester': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['college.Semester']", 'null': 'True', 'blank': 'True'})
        },
        u'college.coursebranch': {
            'Meta': {'object_name': 'CourseBranch'},
            'branch': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'college.qualifiedexam': {
            'Meta': {'object_name': 'QualifiedExam'},
            'authority': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'college.semester': {
            'Meta': {'object_name': 'Semester'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'semester': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'college.technicalqualification': {
            'Meta': {'object_name': 'TechnicalQualification'},
            'authority': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'})
        },
        u'fees.commonfeespayment': {
            'Meta': {'object_name': 'CommonFeesPayment'},
            'head': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fees.FeesHead']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'paid_amount': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '14', 'decimal_places': '2'}),
            'paid_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['admission.Student']", 'null': 'True', 'blank': 'True'})
        },
        u'fees.feeshead': {
            'Meta': {'object_name': 'FeesHead'},
            'amount': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '14', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'fees.feespayment': {
            'Meta': {'object_name': 'FeesPayment'},
            'fee_structure': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fees.FeesStructure']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'payment_installment': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['fees.FeesPaymentInstallment']", 'null': 'True', 'blank': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['admission.Student']", 'null': 'True', 'blank': 'True'})
        },
        u'fees.feespaymentinstallment': {
            'Meta': {'object_name': 'FeesPaymentInstallment'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'installment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fees.Installment']", 'null': 'True', 'blank': 'True'}),
            'installment_amount': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '14', 'decimal_places': '2'}),
            'installment_fine': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '14', 'decimal_places': '2'}),
            'paid_amount': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '14', 'decimal_places': '2'}),
            'paid_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['admission.Student']", 'null': 'True', 'blank': 'True'}),
            'total_amount': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '14', 'decimal_places': '2'})
        },
        u'fees.feesstructure': {
            'Meta': {'object_name': 'FeesStructure'},
            'batch': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['college.Batch']", 'null': 'True', 'blank': 'True'}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['college.Course']", 'null': 'True', 'blank': 'True'}),
            'head': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['fees.FeesStructureHead']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'fees.feesstructurehead': {
            'Meta': {'object_name': 'FeesStructureHead'},
            'amount': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '14', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'installments': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['fees.Installment']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'no_installments': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'fees.installment': {
            'Meta': {'object_name': 'Installment'},
            'amount': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '14', 'decimal_places': '2'}),
            'due_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fine_amount': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '14', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['fees']