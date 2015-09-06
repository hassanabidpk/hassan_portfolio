# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post_author', models.CharField(max_length=250)),
                ('post_name', models.CharField(max_length=400)),
                ('post_title', models.CharField(max_length=400)),
                ('post_photo', models.ImageField(upload_to=b'posts', blank=True)),
                ('post_content', models.TextField()),
                ('post_modified', models.DateTimeField(auto_now=True, verbose_name=b'date modified')),
                ('post_published', models.DateTimeField(auto_now_add=True, verbose_name=b'date published')),
                ('post_type', models.CharField(max_length=200)),
                ('comment_count', models.IntegerField(default=0)),
                ('post_category', models.CharField(default=b'programming', max_length=200)),
                ('post_tags', models.CharField(default=b'code', max_length=200)),
                ('post_code', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True, max_length=60)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('news_author', models.CharField(max_length=250)),
                ('news_title', models.CharField(max_length=400)),
                ('news_contens', models.TextField()),
                ('news_url', models.URLField(max_length=300)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('news_type', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True, max_length=60)),
                ('category', models.ManyToManyField(to='portfolio.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('github_link', models.URLField(max_length=300, blank=True)),
                ('android', models.URLField(max_length=300, blank=True)),
                ('ios', models.URLField(max_length=300, blank=True)),
                ('web', models.URLField(max_length=300, blank=True)),
                ('slug', models.SlugField(unique=True, max_length=120)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('related_projects', models.CharField(max_length=400)),
                ('logo', models.ImageField(upload_to=b'posts/skills', blank=True)),
                ('term', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True, max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='skills',
            field=models.ManyToManyField(to='portfolio.Skill'),
        ),
        migrations.AddField(
            model_name='project',
            name='writer',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ManyToManyField(to='portfolio.Category'),
        ),
        migrations.AddField(
            model_name='blog',
            name='writer',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
