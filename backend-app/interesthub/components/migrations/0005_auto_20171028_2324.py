# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 20:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0004_auto_20171028_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='long_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='component',
            name='small_text',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='component',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]