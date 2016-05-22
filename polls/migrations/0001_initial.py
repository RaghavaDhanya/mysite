# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 19:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_desc', models.CharField(max_length=200)),
                ('task_status', models.CharField(max_length=200)),
                ('task_priority', models.IntegerField(default=3)),
                ('task_Due', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=200)),
                ('task_createDate', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.AddField(
            model_name='taskdetails',
            name='Tasks',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Tasks'),
        ),
    ]