# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0020_auto_20170308_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking_info',
            name='total_seats',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='user_sel',
            name='booking',
            field=models.ForeignKey(default=1, to='movieapp.Booking_info'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user_sel',
            name='selected_seats',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='user_sel',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
