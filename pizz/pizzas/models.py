from django.db import models

# Create your models here.

class Pizza(models.Model):
	'''a class to hold the names of pizzas'''
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True) 

	def __str__(self):
		'''return a string representation of the module'''
		return self.text
		 
class Topping(models.Model):
	'''tell about the toppings of the pizza'''
	topic = models.ForeignKey('Pizza', on_delete=models.PROTECT)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
	
	class meta:
		verbose_name_plural = 'entries'
	
	def __str__(self):
		'''returning a string representation of model'''
		if self.text[50:]:
			return self.text[:50]+'...'
		else:
			return self.text
