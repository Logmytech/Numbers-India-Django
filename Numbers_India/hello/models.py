from django.db import models

# Create your models here.

class mobileNumbers(models.Model):
	number = models.()
	full_name = models.CharField(max_length=120, blank=True, null=False)

	def __unicode__(self): #Python 3.3 is __str__
		return self.number
