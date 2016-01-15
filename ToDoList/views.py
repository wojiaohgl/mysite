from django.shortcuts import render
from ToDoList.models import *
from django.shortcuts import render_to_response
from django.template import RequestContext

def itemsList(request):
	toDoList=ToDoItem.objects.order_by('-status')
	return render_to_response('toDoList.html', {'toDoList':toDoList}, context_instance = RequestContext(request))

