from django.conf.urls import url, include
from . import views

urlpatterns = [
		#home page
		url(r'^$', views.index, name='index'),
		]
