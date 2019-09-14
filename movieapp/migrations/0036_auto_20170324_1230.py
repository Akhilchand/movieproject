# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0035_auto_20170322_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='seats',
            name='cost_of_ticket',
            field=models.DecimalField(default=0, null=True, max_digits=10, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='seats',
            name='seat',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='seats',
            name='seat_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='seats',
            name='show',
            field=models.ForeignKey(blank=True, to='movieapp.Booking_info', null=True),
        ),
    ]
