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
	]

