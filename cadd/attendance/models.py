from jsonfield import JSONField

from django.db import models

from admission.models import Student 
from college.models import Batch
from staff.models import Staff

CHOICES = (
	('Absent', 'Absent'),
	('Present', 'Present'),
)


class Attendance(models.Model):

	batch = models.ForeignKey(Batch, null=True, blank=True)
	teacher = models.ForeignKey(Staff, null=True, blank=True)
	student = models.ForeignKey(Student, null=True, blank=True)
	status = models.CharField('Status', null=True, blank=True, max_length=30, choices=CHOICES)
	
	date = models.DateField('Date', null=True, blank=True)

	def __unicode__(self):

		return self.student.student_name + str(self.date)

	class Meta:

		verbose_name_plural = 'Attendance'

class HolidayCalendar(models.Model):

	date = models.DateField('Date', null=True, blank=True)
	is_holiday = models.BooleanField('Is holiday', default=False)
	
	def __unicode__(self):

		return str(self.date) 

	class Meta:

		verbose_name_plural = 'Holiday Calendar'


