from django.db import models
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from django.template.defaultfilters import slugify



class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=60, unique=True)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/categories/%s/" % self.slug

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        return super(Category,self).save(*args, **kwargs)


class Post(models.Model):
	post_author = models.ForeignKey(User,limit_choices_to={'is_staff': True})
	post_name = models.CharField(max_length=400)
	post_title = models.CharField(max_length=400)
	post_photo = models.ImageField(upload_to='posts',blank=True)
	post_content = models.TextField()
	post_modified =  models.DateTimeField('date modified',auto_now=True)
	post_published =  models.DateTimeField('date published',auto_now_add=True)
	post_type = models.CharField(max_length=200)
	category = models.ManyToManyField(Category)
	comment_count = models.IntegerField(default=0)
	post_code = models.TextField(default="")

	class Meta:
		verbose_name_plural = "Posts"

	def __str__(self):
		return self.post_title

	def save(self,*args, **kwargs):
		if not self.id:
			self.post_name = self.post_title
		return super(Post,self).save(*args, **kwargs)

	def next(self):
		try:
			return get_object_or_404(Post,pk=self.pk+1)
		except:
			return None
	def previous(self):
		try :
			return get_object_or_404(Post,pk=self.pk-1)
		except:
			return None


class Skill(models.Model):

	title = models.CharField(max_length=250)
	related_projects = models.CharField(max_length=400)
	logo = models.ImageField(upload_to='posts/skills',blank=True)
	term = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100, unique=True)

	def __str__(self):
		return self.title


	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.title)
		return super(Skill,self).save(*args, **kwargs)

class Project(models.Model):

    title = models.CharField(max_length=300)
    description = models.TextField()
    github_link = models.URLField(max_length=300,blank=True)
    android = models.URLField(max_length=300,blank=True)
    ios = models.URLField(max_length=300,blank=True)
    web = models.URLField(max_length=300,blank = True)
    skills  = models.ManyToManyField(Skill)
    writer = models.ForeignKey(User,limit_choices_to={'is_staff': True})
    slug = models.SlugField(max_length=120, unique=True)
    updatedAt =  models.DateTimeField(auto_now=True)
    createdAt =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        return super(Project,self).save(*args, **kwargs)


class News(models.Model):

	news_author = models.CharField(max_length=250)
	news_title = models.CharField(max_length=400)
	news_contens = models.TextField()
	news_url = models.URLField(max_length=300)
	updatedAt =  models.DateTimeField(auto_now=True)
	createdAt =  models.DateTimeField(auto_now_add=True)
	news_type = models.CharField(max_length=200)
	category = models.ManyToManyField(Category)
	slug = models.SlugField(max_length=60, unique=True)

	class Meta:
		verbose_name_plural = "News"
	def __str__(self):
		return news_title

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.news_title)
		return super(News,self).save(*args, **kwargs)
