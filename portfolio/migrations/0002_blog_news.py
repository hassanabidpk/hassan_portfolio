# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post_author', models.CharField(max_length=250)),
                ('post_name', models.CharField(max_length=400)),
                ('post_title', models.CharField(max_length=400)),
                ('post_content', models.TextField()),
                ('post_modified', models.DateTimeField(verbose_name=b'date modified')),
                ('post_published', models.DateTimeField(verbose_name=b'date published')),
                ('post_type', models.CharField(max_length=200)),
                ('comment_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('news_author', models.CharField(max_length=250)),
                ('news_title', models.CharField(max_length=400)),
                ('news_contens', models.TextField()),
                ('news_url', models.URLField(max_length=300)),
                ('news_published', models.DateTimeField(verbose_name=b'date published')),
                ('news_type', models.CharField(max_length=200)),
            ],
        ),
    ]
