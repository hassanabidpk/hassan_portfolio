import datetime

from django.db import models
from django.utils import timezone




class Hack(models.Model):
	hack_title = models.CharField(max_length=400)
	hack_description = models.TextField()
	hack_link = models.URLField()
	hack_photo = models.ImageField(upload_to='posts/hacks',blank=True)
	hack_code  = models.TextField()

	def __str__(self):
		return hack_title

class HackCat(models.Model):
	hack = models.ForeignKey(Hack)
	cat_title = models.CharField(max_length=250, default ="programming")
	cat_pos = models.IntegerField(default=0)
	cat_description  = models.CharField(max_length=400)

	def __str__(self):
		return self.cat_title


