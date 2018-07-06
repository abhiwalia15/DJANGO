from django import forms

from .models import Topic, Entry

#now we define a class called TopicForm, which inherits from forms.ModelForm.
class TopicForm(forms.ModelForm):
	#The simplest version of a ModelForm consists of a nested Meta class 
	class Meta:
		model = Topic
		fields = ['text']
		labels = {'text':''}

class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ['text']
		labels = {'text':''}
		#A widget is an HTML form element, such as a single-line text box, multi-line text area, or drop-down list.
		#By telling Django to use a forms.Textarea element, we’re customizing the input widget for the field 'text' 
		#so the text area will be 80 columns wide instead of the default 40.
		widgets = {'text':forms.Textarea(attrs={'cols':80})}
