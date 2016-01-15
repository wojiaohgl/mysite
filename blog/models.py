from django.db import models
from django.contrib import admin

class BlogPost(models.Model):
	class Meta:
		ordering=('timestamp',)
	title=models.CharField(max_length=150)
	body=models.TextField()
	timestamp=models.DateTimeField()
	def __unicode__(self):
		return self.title
class BlogComment(models.Model):
	blogPost=models.ForeignKey(BlogPost)
	user=models.TextField()
	body=models.TextField()
	timestamp=models.DateTimeField()
	def __unicode__(self):
		return self.body
class SiteComment(models.Model):
	user=models.TextField()
	body=models.TextField()
	timestamp=models.DateTimeField()
	def __unicode__(self):
		return self.body
