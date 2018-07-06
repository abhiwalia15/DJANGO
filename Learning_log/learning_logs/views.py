from django.shortcuts import render
from .models import Topic

'''A view function takes in information from a request, prepares the data 
needed to generate a page, and then sends the data back to the browser, 
often by using a template that defines what the page will look like.'''

def index(request):
	'''the home page for learning logs'''
	return render(request, 'learning_logs/index.html')

def topics(request):
	'''show all topics'''
	topics = Topic.objects.order_by('date_added')
	context = {'topics':topics}
	return render(request, 'learning_logs/topics.html', context)

'''This is the first view function that requires a parameter other than the request object
The function accepts the value captured by the 
expression (?P<topic_id>\d+) and stores it in topic_id'''

def topic(request, topic_id):
	'''show a single topic and all its entries'''
	topic = Topic.objects.get(id = topic_id)
	#the minus sign infront of the date_added sorts the result in reverse order, which will display the most recent entries first.
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic': topic, 'entries': entries}
	return render(request, 'learning_logs/topic.html', context)
