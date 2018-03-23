# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0002_auto_20180315_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empaddr',
            name='Address1',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='empaddr',
            name='Address2',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='empaddr',
            name='Employee',
            field=models.ForeignKey(to='details.Employee', null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='Email',
            field=models.EmailField(unique=True, max_length=254),
        ),
    ]
