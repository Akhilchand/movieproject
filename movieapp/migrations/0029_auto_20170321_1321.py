# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0028_seat_movie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seat',
            name='movie',
        ),
        migrations.AddField(
            model_name='seat',
            name='seat_status',
            field=models.CharField(default=b'N', max_length=50, choices=[(b'S', b'Selected'), (b'N', b'Not_Selected')]),
        ),
        migrations.AlterField(
            model_name='user_sel',
            name='booking',
            field=models.ForeignKey(to='movieapp.Booking_info'),
        ),
    ]
