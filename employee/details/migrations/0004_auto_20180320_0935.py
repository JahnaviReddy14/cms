# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0003_auto_20180315_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='empaddr',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='empaddr',
            name='modified_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='employee',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='employee',
            name='modified_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
