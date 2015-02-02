# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassicEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_datetime', models.DateField()),
                ('end_datetime', models.DateField()),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Classic Event',
                'verbose_name_plural': 'Classic Events',
            },
            bases=(models.Model,),
        ),
    ]
