# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import MovieLib.models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieLib', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='todo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('What', models.CharField(max_length=128)),
                ('Deadline', models.DateField()),
                ('Done', MovieLib.models.IntegerRangeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='movie',
            name='genre',
        ),
        migrations.AlterField(
            model_name='movie',
            name='price',
            field=MovieLib.models.IntegerRangeField(),
        ),
    ]
