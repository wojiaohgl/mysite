from django.conf.urls import *
from ToDoList.views import * 

urlpatterns=patterns('',
		url(r'^$',itemsList),
		)
