# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20150628_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='post_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 28, 14, 40, 58, 81181), verbose_name=b'date modified'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='post_published',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 28, 14, 40, 58, 81249), verbose_name=b'date published'),
        ),
    ]
