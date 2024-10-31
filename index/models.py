from django.db import models

class Contact(models.Model):
	name = models.CharField(max_length=50)
	subject = models.CharField(max_length=50)
	email = models.EmailField()
	message = models.TextField()

	def __str__ (self):
		return self.email


class whatsapp(models.Model):
	number  = models.CharField(max_length=200,default='')
	def __dtr__ (self):
		return self.number
