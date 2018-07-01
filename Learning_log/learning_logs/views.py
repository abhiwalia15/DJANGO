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
