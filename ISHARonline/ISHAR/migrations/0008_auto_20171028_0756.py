# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 07:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ISHAR', '0007_auto_20171028_0755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='issue',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
