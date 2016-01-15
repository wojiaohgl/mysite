from django.shortcuts import render,render_to_response
from django.contrib.auth import logout,login,authenticate
from django.http import HttpResponse,HttpResponseRedirect
from blog.models import BlogPost
from blog.models import BlogComment
from blog.models import SiteComment
from django.template import loader,Context,RequestContext
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
def archive(request):
	postandcomment=[]
	posts=BlogPost.objects.all()
	for post in posts:
		comments=post.blogcomment_set.all()
		tempList=[post,comments]
		postandcomment.append(tempList)
	t=loader.get_template("archive.html")
	c=Context({'posts':postandcomment,'user':request.user})
	#return HttpResponse(t.render(c))
	return render_to_response('archive.html', {'posts':postandcomment,'user':request.user}, context_instance = RequestContext(request))

@login_required(login_url='/admin')
def addComment(request):
	body=request.GET['q']
	blogPost_id=request.GET['blogId']
	user=request.GET['userName']
	newComment=BlogComment(user=user,body=body,timestamp=datetime.datetime.now(),blogPost_id=blogPost_id)
	newComment.save()
	return HttpResponseRedirect('/blog')
def my_logout(request):
	logout(request)
	return HttpResponseRedirect('/blog')
def oweMeKiss(request):
	t=loader.get_template("note.html")
	c=Context({})
	return HttpResponse(t.render(c))
def myRegist(request):
	username=request.GET['newUserName']
	password=request.GET['newUserPW']
	user=User.objects.create_user(username=username,password=password)
	user.is_staff=1
	user.save()
	user=authenticate(username=username, password=password)
	login(request,user)
	return HttpResponseRedirect('/blog')
def siteComment(request):
	posts=SiteComment.objects.all()
	return render_to_response('siteComment.html', {'posts':posts,'user':request.user}, context_instance = RequestContext(request))

def addSiteComment(request):
	body=request.GET['q']
	user=request.GET['userName']
	newComment=SiteComment(user=user,body=body,timestamp=datetime.datetime.now())
	newComment.save()
	return HttpResponseRedirect('/siteComment')
