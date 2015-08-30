import datetime
from django.db import models
from django.utils import timezone

class Blog(models.Model):
	post_author = models.CharField(max_length=250)
	post_name = models.CharField(max_length=400)
	post_title = models.CharField(max_length=400)
	post_photo = models.ImageField(upload_to='posts',blank=True)
	post_content = models.TextField()
	post_modified =  models.DateTimeField('date modified',auto_now=True)
	post_published =  models.DateTimeField('date published',auto_now_add=True)
	post_type = models.CharField(max_length=200)
	comment_count = models.IntegerField(default=0)
	post_category = models.CharField(max_length=200, default="programming")
	post_tags = models.CharField(max_length=200,default="code")
	post_code = models.TextField(default="")

	def __str__(self):
		return self.post_title

	def save(self):
		if not self.id:
			pass 
		return super(Blog,self).save()

	def next(self):
		try:
			return Blog.objects.get(pk=self.pk+1)
		except:
			return None
	def previous(self):
		try :
			return Blog.objects.get(pk=self.pk-1)
		except:
			return None

class News(models.Model):
	
	news_author = models.CharField(max_length=250)
	news_title = models.CharField(max_length=400)
	news_contens = models.TextField()
	news_url = models.URLField(max_length=300)
	news_published = models.DateTimeField('date published')
	news_type = models.CharField(max_length=200)

	def __str__(self):
		return news_title






