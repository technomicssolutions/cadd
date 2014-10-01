from django.db import models
from django.contrib.auth.models import User

ROLE = (
	('teacher', 'Teacher'),
	('staff', 'Staff'),
)
class Permission(models.Model):

	attendance_module = models.BooleanField('Attendance Permission', default=False)
	admission_module = models.BooleanField('Admission Permission', default=False)
	college_module = models.BooleanField('College Permission', default=False)
	fees_module = models.BooleanField('Fees Permission', default=False)
	
	class Meta:
		verbose_name_plural = 'Permission'

class Staff(models.Model):
	user = models.ForeignKey(User, null=True, blank=True)
	permission = models.ForeignKey(Permission, null=True, blank=True)

	dob = models.DateField('Date of Birth',null=True, blank=True)
	address= models.TextField('Staff Address',null=True, blank=True, max_length=200)
	mobile_number= models.CharField('Mobile Number',null=True, blank=True, max_length=200)
	land_number= models.CharField('Land Number',null=True, blank=True, max_length=200)
	
	blood_group = models.CharField('Blood Group',null=True, blank=True, max_length=200)
	doj = models.DateField('Date of Join',null=True, blank=True)
	qualifications = models.TextField('Qualifications',null=True, blank=True, max_length=200)
	experiance = models.CharField('Experiance',null=True, blank=True, max_length=200)
	photo = models.ImageField(upload_to = "uploads/photos/", null=True, blank=True)
	
	role = models.CharField('Role',null=True, blank=True, max_length=200, choices=ROLE)

	def __unicode__(self):
		return (self.staff.user.first_name + str(' ') + self.staff.user.last_name)

	class Meta:
		verbose_name = 'Staff'
		verbose_name_plural = 'Staff'





