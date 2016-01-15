from django.conf.urls import *
from blog.views import * 

urlpatterns=patterns('',
		url(r'^$',archive),
		url(r'^addComment$',addComment),
		url(r'^addSiteComment$',addSiteComment),
		)
