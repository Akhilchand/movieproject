# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0018_booking_info_seat_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking_info',
            name='seat_num',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='user_sel',
            name='selected_seats',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
    ]
