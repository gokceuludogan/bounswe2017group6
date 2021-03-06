# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-18 14:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('content', '0011_comment_updown'),
        ('user', '0008_auto_20171117_1839'),
        ('group', '0009_auto_20171118_1703'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('url', models.URLField()),
                ('contents', models.ManyToManyField(related_name='tags', to='content.Content')),
                ('groups', models.ManyToManyField(related_name='tags', to='group.InterestGroup')),
                ('users', models.ManyToManyField(related_name='interests', to='user.UserProfile')),
            ],
        ),
    ]
