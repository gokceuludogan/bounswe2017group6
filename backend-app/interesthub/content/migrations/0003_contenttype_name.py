# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 20:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_remove_content_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='contenttype',
            name='name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
