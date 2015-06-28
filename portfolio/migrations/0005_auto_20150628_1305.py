# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20150622_0403'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='post_category',
            field=models.CharField(default=b'programming', max_length=200),
        ),
        migrations.AddField(
            model_name='blog',
            name='post_code',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='blog',
            name='post_tags',
            field=models.CharField(default=b'code', max_length=200),
        ),
        migrations.AlterField(
            model_name='blog',
            name='post_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 28, 13, 5, 22, 9837), verbose_name=b'date modified'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='post_published',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 28, 13, 5, 22, 9867), verbose_name=b'date published'),
        ),
    ]
