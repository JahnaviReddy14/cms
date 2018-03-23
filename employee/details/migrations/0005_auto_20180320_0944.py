# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0004_auto_20180320_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empaddr',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='empaddr',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
