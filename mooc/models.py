from django.db import models
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from django.template.defaultfilters import slugify



class MOOC(models.Model):
    course_title = models.CharField(max_length=350)
    course_provider = models.CharField(max_length=100)
    course_certificate = models.ImageField(upload_to='posts/certificates',blank=True)
    course_completion_date = models.DateTimeField()
    course_summary = models.TextField(null=True, blank=True)
    course_certificate_link = models.URLField(max_length=350,blank=True)
    course_github_link = models.URLField(max_length=300,blank=True)
    class Meta:
        verbose_name_plural = "Moocs"

    def __str__(self):
        return self.course_title + " | " + self.course_provider
