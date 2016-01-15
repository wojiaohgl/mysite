#encoding:utf-8
from django.contrib import admin
from django.core.mail import send_mail
from blog.models import BlogPost
from blog.models import BlogComment
from blog.models import SiteComment

#class BlogPostInline(admin.StackedInline):
#	model=BlogPost
#	extra=3

class BlogPostAdmin(admin.ModelAdmin):
	#fieldsets=[(None,{'fields':['title','body']}),('Date information',{'fields':['timestamp'],'classes':['collapse']}),]
	#fieldsets=[(None,{'fields':['title','body']}),('Date information',{'fields':['timestamp']}),]
	list_display=('title','timestamp')
	list_filter=['timestamp']
	#search_fields=['title']
	#date_hierarchy='timestamp'
	#inlines=[BlogPostInline]
	def save_model(self, request, obj, form, change):
		obj.user = request.user
		send_mail(subject=u"wojiaohgl.com今日更新:  "+obj.title,message=obj.body,from_email='wojiaohgl@126.com',recipient_list=['598137115@qq.com','1542567400@qq.com'],auth_user='wojiaohgl',auth_password='14524beyondecho1')
		obj.save()

admin.site.register(BlogPost,BlogPostAdmin)
admin.site.register(SiteComment)
admin.site.register(BlogComment)

