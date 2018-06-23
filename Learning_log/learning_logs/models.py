from django.db import models

# Create your models here.
class Topic(models.Model):
	'''a topic user is learning about'''
	#CharField—a piece of data that’s made up of characters, or text
	#You use CharField when you want to store a small amount of text, 
	#such as a name, a title, or a city
	text = models.CharField(max_length = 200)
	
	#The date_added attribute is a DateTimeField—a piece of 
	#data that will record a date and time
	date_added = models.DateTimeField(auto_now_add = True)
	
	def __str__(self):
		'''return a string representation of the module'''
		return self.text 
