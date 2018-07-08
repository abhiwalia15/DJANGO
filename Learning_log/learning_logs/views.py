from django.shortcuts import render
from .models import Topic, Entry

'''We import the class HttpResponseRedirect, which we’ll use to redirect 
the reader back to the topics page after they submit their topic. 
The reverse() function determines the URL from a named URL pattern, 
meaning that Django will generate the URL when the page is requested.'''
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TopicForm, EntryForm

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

def new_topic(request):
	'''add a new topic'''
	if request.method != 'POST':
		#no data is submitted; create a blank form.
		form = TopicForm()
		
	else:
		#post data submitted; process data.
		form = TopicForm(request.POST)
	
	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('learning_logs:topics'))
		
	context = { 'form':form }
	return render(request, 'learning_logs/new_topic.html', context)
		
def new_entry(request, topic_id):
	'''add a new entry for a particular topic'''
	topic = Topic.objects.get(id=topic_id)
	if request.method != 'POST':
		#no data submitted; create a blank form
		form = EntryForm()
		
	else:
		form = EntryForm(data = request.POST)
		
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.topic = topic
			new_entry.save()
			return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))
			
	context = {'topic':topic, 'form':form}
	return render(request, 'learning_logs/new_entry.html', context)

def edit_entry(request, entry_id):
	'''edit an existing entry'''
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic
	
	if request.method != 'POST':
		#initial request; pre-fill form with the current entry.
		form = EntryForm(instance=entry)
		
	else:
		#POST data submitted; process data.
		form = EntryForm(instance=entry, data=request.POST)
		
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))
			
	context = {'entry':entry, 'topic':topic, 'form':form}
	return render(request, 'learning_logs/edit_entry.html', context)
			
