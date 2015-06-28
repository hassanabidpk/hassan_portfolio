# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20150502_0824'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='post_photo',
            field=models.ImageField(default='media/posts/default.jpg', upload_to=b'posts'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='post_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 22, 3, 59, 25, 932615), verbose_name=b'date modified'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='post_published',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 22, 3, 59, 25, 932677), verbose_name=b'date published'),
        ),
    ]
