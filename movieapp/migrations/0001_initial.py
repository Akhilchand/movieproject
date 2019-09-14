# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieCategory',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='MovieDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hero', models.CharField(max_length=30, null=True, blank=True)),
                ('heroine', models.CharField(max_length=30, null=True, blank=True)),
                ('director', models.CharField(max_length=30, null=True, blank=True)),
                ('musicdirector', models.CharField(max_length=30, null=True, blank=True)),
                ('producer', models.CharField(max_length=30, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('movie_name', models.CharField(max_length=30, null=True, blank=True)),
                ('category', models.CharField(max_length=30, null=True, blank=True)),
                ('release_date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='moviedetails',
            name='movie_id',
            field=models.ForeignKey(to='movieapp.Movies', null=True),
        ),
        migrations.AddField(
            model_name='moviecategory',
            name='movie_category',
            field=models.ForeignKey(to='movieapp.Movies', null=True),
        ),
    ]
