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
            name='Hack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('short_description', models.CharField(max_length=400)),
                ('long_description', models.TextField()),
                ('github_link', models.URLField(max_length=250, blank=True)),
                ('ppt_link', models.URLField(max_length=250, blank=True)),
                ('slug', models.SlugField(unique=True, max_length=100)),
                ('cover_photo', models.ImageField(upload_to=b'posts/hacks')),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='HackCat',
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
        migrations.AddField(
            model_name='hack',
            name='category',
            field=models.ManyToManyField(to='hacks.HackCat'),
        ),
        migrations.AddField(
            model_name='hack',
            name='writer',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
