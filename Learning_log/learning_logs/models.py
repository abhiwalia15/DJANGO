from django.db import models
from django.contrib.auth.models import User 

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
	#add an owner field to Topic, which establishes a foreign key relationship to the User model
	owner = models.ForeignKey('users', on_delete=models.PROTECT)

	def __str__(self):
		"""Return a string representation of the model."""
		return self.text
	
class Entry(models.Model):
	'''something specific learned about the topic'''
	'''A foreign key is a database term; it’s a reference to another record in the database. 
	This is the code that connects each entry to a specific topic.
	 Each topic is assigned a key, or ID, when it’s created.
	'''
	topic = models.ForeignKey('Topic', on_delete=models.PROTECT)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		'''Meta holds extra information for managing a model; 
		here it allows us to set a special attribute telling Django to 
		use Entries when it needs to refer to more than one entry. 
		'''
		verbose_name_plural = 'entries'
	
	def __str__(self):
		'''return a string representation of the module'''
		if self.text[50:]:
			return self.text[:50]+'...'
		else:
			return self.text
	
