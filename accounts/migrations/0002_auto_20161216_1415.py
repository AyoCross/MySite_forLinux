# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-16 14:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='twitter',
            new_name='zhihu',
        ),
        migrations.AlterField(
            model_name='socialinfo',
            name='social',
            field=models.CharField(choices=[('fa-facebook', 'Facebook'), ('fa-github', 'Github'), ('fa-zhihu', 'Zhihu'), ('fa-google-plus', 'Google Plus'), ('fa-weibo', 'Weibo')], max_length=128),
        ),
    ]
