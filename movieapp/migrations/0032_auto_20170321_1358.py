# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0031_remove_seat_seat_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seat',
            name='show',
        ),
        migrations.AddField(
            model_name='booking_info',
            name='seat_num',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='booking_info',
            name='total_seats',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.DeleteModel(
            name='Seat',
        ),
    ]
