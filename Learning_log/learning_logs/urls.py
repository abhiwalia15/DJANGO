'''Define URL patterns for Learning_Logs'''

from django.conf.urls import url, include
#the dot tells Python to import views from the same directory as the current urls.py module.
from . import views

'''r'^$'. The r tells Python to interpret the following string as a raw string, 
		and the quotes tell Python where the regular expression begins and ends.
		 The caret (^) tells Python to find the beginning of the string,
		 and the dollar sign tells Python to look for the end of the string.'''
urlpatterns = [
		#home page
		url(r'^$', views.index, name='index'),
		#show all topics.
		url(r'^topics/$', views.topics, name='topics'),
		#DETAILS PAGE FOR SINGLE topic.
		url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
		#page for adding a new topic.
		url(r'^new_topic/$', views.new_topic, name='new_topic'),
		#page for adding a new entry.
		#The code (?P<topic_id>\d+) captures a numerical value and stores it in the variable topic_id
		url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
	]
	

