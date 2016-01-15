from django.db import models
from django.contrib.auth.models import User

class ToDoItem(models.Model):
	class Meta:
		ordering=('timestamp',)
	title=models.CharField(max_length=150)
	body=models.TextField()
	timestamp=models.DateTimeField()
	passStatu=models.NullBooleanField(default=True)
	reward=models.TextField()
	status=models.BooleanField(default=True)
	rewarder=models.ForeignKey(User)
	def __unicode__(self):
		return self.title
	
