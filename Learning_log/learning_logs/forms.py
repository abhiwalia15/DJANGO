from django import forms

from .models import Topic

#now we define a class called TopicForm, which inherits from forms.ModelForm.
class TopicForm(forms.ModelForm):
	#The simplest version of a ModelForm consists of a nested Meta class 
	class Meta:
		model = Topic
		fields = ['text']
		labels = {'text':''}
