# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0039_auto_20170324_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingtransactions',
            name='seat_selected',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='bookingtransactions',
            name='seat',
            field=models.ForeignKey(blank=True, to='movieapp.Booking_info', null=True),
        ),
    ]
