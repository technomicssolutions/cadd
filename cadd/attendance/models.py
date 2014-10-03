from jsonfield import JSONField

from django.db import models
from django.contrib.auth.models import User

from admission.models import Student 
from college.models import Batch
from staff.models import Staff

CHOICES = (
	('Absent', 'Absent'),
	('Present', 'Present'),
)

class Attendance(models.Model):

	user = models.ForeignKey(User)
	batch = models.ForeignKey(Batch, null=True, blank=True)
	topics_covered = models.CharField('Topics Covered', null=True, blank=True, max_length=200)
	remarks = models.CharField('Remarks', null=True, blank=True, max_length=200)
	date = models.DateField('Date', null=True, blank=True)

	def __unicode__(self):

		return self.batch.name + str(self.date)

	class Meta:

		verbose_name_plural = 'Attendance'

class StudentAttendance(models.Model):

	attendance  = models.ForeignKey(Attendance)
	student = models.ForeignKey(Student, null=True, blank=True)
	status = models.CharField('Status', null=True, blank=True, max_length=30, choices=CHOICES)

	def __unicode__(self):

		return self.student.student_name + str(self.attendance.date)

	class Meta:

		verbose_name_plural = 'Student Attendance'

class HolidayCalendar(models.Model):

	date = models.DateField('Date', null=True, blank=True)
	is_holiday = models.BooleanField('Is holiday', default=False)
	
	def __unicode__(self):

		return str(self.date) 

	class Meta:

		verbose_name_plural = 'Holiday Calendar'


