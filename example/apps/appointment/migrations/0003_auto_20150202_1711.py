# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_classicevent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classicevent',
            name='end_datetime',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='classicevent',
            name='start_datetime',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
