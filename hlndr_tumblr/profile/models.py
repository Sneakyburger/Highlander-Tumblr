from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
	
	def __unicode__(self):
		return user.username
		
