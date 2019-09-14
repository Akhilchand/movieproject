# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hero', models.CharField(max_length=30, null=True, blank=True)),
                ('heroine', models.CharField(max_length=30, null=True, blank=True)),
                ('director', models.CharField(max_length=30, null=True, blank=True)),
                ('musicdirector', models.CharField(max_length=30, null=True, blank=True)),
                ('producer', models.CharField(max_length=30, null=True, blank=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Movies',
            new_name='Movie',
        ),
        migrations.RemoveField(
            model_name='moviedetails',
            name='movie_id',
        ),
        migrations.DeleteModel(
            name='MovieDetails',
        ),
        migrations.AddField(
            model_name='moviedetail',
            name='movie_id',
            field=models.ForeignKey(to='movieapp.Movie', null=True),
        ),
    ]
