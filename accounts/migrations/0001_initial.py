# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-11 12:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=128)),
                ('biography', models.TextField(blank=True, null=True)),
                ('homepage', models.URLField(blank=True, null=True)),
                ('weixin', models.URLField(blank=True, null=True)),
                ('douban', models.URLField(blank=True, null=True)),
                ('weibo', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('github', models.URLField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SocialInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social', models.CharField(choices=[('fa-facebook', 'Facebook'), ('fa-github', 'Github'), ('fa-twitter', 'Twitter'), ('fa-google-plus', 'Google Plus'), ('fa-weibo', 'Weibo')], max_length=128)),
                ('url', models.URLField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]