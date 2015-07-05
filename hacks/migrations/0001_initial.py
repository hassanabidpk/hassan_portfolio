# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hack_title', models.CharField(max_length=400)),
                ('hack_description', models.TextField()),
                ('hack_link', models.URLField()),
                ('hack_photo', models.ImageField(upload_to=b'posts/hacks', blank=True)),
                ('hack_code', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HackCat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cat_title', models.CharField(default=b'programming', max_length=250)),
                ('cat_pos', models.IntegerField(default=0)),
                ('cat_description', models.CharField(max_length=400)),
                ('hack', models.ForeignKey(to='hacks.Hack')),
            ],
        ),
    ]
