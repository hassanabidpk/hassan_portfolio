# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
        migrations.CreateModel(
            name='Views',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('views', models.IntegerField(default=0)),
                ('resume', models.ForeignKey(to='portfolio.Resume')),
            ],
        ),
    ]
