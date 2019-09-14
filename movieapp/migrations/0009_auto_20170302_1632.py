# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0008_seat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('show_details', models.CharField(max_length=30, null=True, blank=True)),
                ('timings', models.DateTimeField(null=True, verbose_name=b'show time')),
                ('movie', models.ForeignKey(to='movieapp.Movie', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='seat',
            name='book',
            field=models.ForeignKey(to='movieapp.Booking', null=True),
        ),
    ]
