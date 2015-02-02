# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SimpleEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Simple Event',
                'verbose_name_plural': 'Simple Events',
            },
            bases=(models.Model,),
        ),
    ]
