from django.db import models

class Software(models.Model):
	name = models.CharField('Software Name', null=True, blank=True, max_length=200, unique=True)
	
	def __unicode__(self):
		return (self.name)

class Course(models.Model):
	name = models.CharField('Course Name', null=True, blank=True, max_length=200)
	software = models.ManyToManyField(Software)
	amount = models.DecimalField('Amount', null=True, blank=True, decimal_places=2, max_digits=10)
	duration = models.CharField('Duration', null=True, blank=True, max_length=200)

	def __unicode__(self):
		return (self.name)

class Batch(models.Model):
	software = models.ForeignKey(Software)
	start_time = models.TimeField('Start Date', null=True, blank=True)
	end_time = models.TimeField('End Date', null=True, blank=True)
	no_of_students = models.IntegerField('No of Students', null=True,blank=True)
	allowed_students = models.IntegerField('Allowed No of Students', null=True,blank=True)

	def __unicode__(self):
		return (self.course.name + ' ' + self.start_date + '-' + self.end_date)
