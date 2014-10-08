from django.db import models
from college.models import Batch, Course
from admission.models import Student, Installment

class FeesHead(models.Model):
	
	name = models.CharField('Head Name', max_length=200, null=True, blank=True)
	amount = models.DecimalField('Amount', max_digits=14, decimal_places=2, default=0)

	def __unicode__(self):

		return str(self.name)
	
	class Meta:

		verbose_name_plural = 'Fees Head'

class FeesStructureHead(models.Model):
	
	name = models.CharField('Head Name', max_length=200, null=True, blank=True)
	amount = models.DecimalField('Amount', max_digits=14, decimal_places=2, default=0)
	no_installments = models.IntegerField('Number of Installments', default=0)
	installments = models.ManyToManyField(Installment, null=True, blank=True)

	def __unicode__(self):

		return str(self.name)
	
	class Meta:

		verbose_name_plural = 'Fees Structure Head'


class FeesStructure(models.Model):
	course = models.ForeignKey(Course, null=True, blank=True)
	head = models.ManyToManyField(FeesStructureHead, null=True, blank=True)
	
	def __unicode__(self):

		return str(self.course.course)
	
	class Meta:

		verbose_name_plural = 'Fees Structure'

class FeesPaymentInstallment(models.Model):
	student = models.ForeignKey(Student, null=True, blank=True)
	total_amount = models.DecimalField('Total Amount', max_digits=14, decimal_places=2, default=0)
	installment = models.ForeignKey(Installment, null=True, blank=True)
	paid_date = models.DateField('Paid Date', null=True, blank=True)
	paid_amount = models.DecimalField('Amount', max_digits=14, decimal_places=2, default=0)
	installment_amount = models.DecimalField('Installment Amount', max_digits=14, decimal_places=2, default=0)
	installment_fine = models.DecimalField('Installment Fine Amount', max_digits=14, decimal_places=2, default=0)

	def __unicode__(self):

		return str(self.total_amount)

	class Meta:

		verbose_name_plural = 'Fees Payment Installment'

class FeesPayment(models.Model):
	
	student = models.ForeignKey(Student, null=True, blank=True)
	payment_installment = models.ManyToManyField(FeesPaymentInstallment, null=True, blank=True)
	
	def __unicode__(self):
		return str(self.student)

	class Meta:

		verbose_name_plural = 'Fees Payment'

class CommonFeesPayment(models.Model):

	student = models.ForeignKey(Student, null=True, blank=True)
	head = models.ForeignKey(FeesHead, null=True, blank=True)
	paid_date = models.DateField('Paid Date', null=True, blank=True)
	paid_amount = models.DecimalField('Paid Amount', max_digits=14, decimal_places=2, default=0)

	def __unicode__(self):
		return str(self.student.student_name) + ' - '+ str(self.head.name)

	class Meta:
		verbose_name_plural = 'Common Fees Payment'