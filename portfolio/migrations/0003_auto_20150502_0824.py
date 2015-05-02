# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_blog_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='post_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 2, 8, 24, 3, 112672), verbose_name=b'date modified'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='post_published',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 2, 8, 24, 3, 112709), verbose_name=b'date published'),
        ),
    ]
