# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movieapp', '0009_auto_20170302_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('show_details', models.CharField(max_length=30, null=True, blank=True)),
                ('timings', models.DateTimeField(null=True, verbose_name=b'show time')),
                ('seat_available', models.IntegerField()),
                ('movie', models.ForeignKey(to='movieapp.Movie', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='user_sel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seats', models.ForeignKey(to='movieapp.Booking_info', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='booking',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='seat',
            name='book',
        ),
        migrations.RenameField(
            model_name='songs',
            old_name='movie_name',
            new_name='movie',
        ),
        migrations.RenameField(
            model_name='songs',
            old_name='track1',
            new_name='track',
        ),
        migrations.RemoveField(
            model_name='songs',
            name='track2',
        ),
        migrations.RemoveField(
            model_name='songs',
            name='track3',
        ),
        migrations.RemoveField(
            model_name='songs',
            name='track4',
        ),
        migrations.AddField(
            model_name='userdetail',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.DeleteModel(
            name='Seat',
        ),
    ]
