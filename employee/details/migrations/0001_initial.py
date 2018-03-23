# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmpAddr',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Address1', models.TextField(max_length=100)),
                ('Address2', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('FirstName', models.CharField(max_length=20)),
                ('LastName', models.CharField(max_length=20)),
                ('Phone_No', models.CharField(max_length=20)),
                ('Email', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='empaddr',
            name='Employee',
            field=models.ForeignKey(to='details.Employee'),
        ),
    ]
