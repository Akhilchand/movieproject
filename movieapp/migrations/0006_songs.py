# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0005_auto_20170228_1542'),
    ]

    operations = [
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tarck1', models.CharField(max_length=30, null=True, blank=True)),
                ('track2', models.CharField(max_length=30, null=True, blank=True)),
                ('track3', models.CharField(max_length=30, null=True, blank=True)),
                ('track4', models.CharField(max_length=30, null=True, blank=True)),
                ('movie_name', models.ForeignKey(to='movieapp.Movie', null=True)),
            ],
        ),
    ]
