from django.db import models
from django.contrib.auth.models import User


class TodoModel(models.Model):

	
	task = models.CharField(max_length=50)
	description = models.TextField(null=True)
	created = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	done = models.BooleanField(default=False)

	def __str__(self):
		return self.task


