from django.db import models

# Create your models here.
class itemGroup(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class item(models.Model):
	name = models.CharField(max_length= 200, null=True)
	price = models.CharField(max_length= 200, null=True)
	description = models.CharField(max_length= 200, null=True)
	group = models.ForeignKey(itemGroup, null=True, on_delete=models.CASCADE)

	def __str__(self):
		return self.name