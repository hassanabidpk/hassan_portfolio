# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-23 07:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MOOC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=350)),
                ('course_provider', models.CharField(max_length=100)),
                ('course_certificate', models.ImageField(blank=True, upload_to='posts/certificates')),
                ('course_completion_date', models.DateTimeField()),
                ('course_summary', models.TextField(blank=True, null=True)),
                ('course_certificate_link', models.URLField(blank=True, max_length=350)),
                ('course_github_link', models.URLField(blank=True, max_length=300)),
            ],
        ),
    ]