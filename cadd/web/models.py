from django.db import models


class Letter(models.Model):

	letter_type = models.CharField('Letter Type',null=True, blank=True, max_length=200)
	date = models.DateField('Date',null=True, blank=True)
	to_address = models.CharField('To Address',null=True, blank=True, max_length=200) 
	from_address = models.CharField('From Address',null=True, blank=True, max_length=200)

	def __unicode__(self):
		return self.letter_type + str('') + self.from_address