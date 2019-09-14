# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0025_auto_20170321_1015'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seat_num', models.CharField(max_length=1000, null=True, blank=True)),
                ('total_seats', models.CharField(max_length=1000, null=True, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='seats',
            name='show',
        ),
        migrations.AddField(
            model_name='booking_info',
            name='seat_available',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.DeleteModel(
            name='Seats',
        ),
        migrations.AddField(
            model_name='seat',
            name='show',
            field=models.ForeignKey(to='movieapp.Booking_info'),
        ),
    ]
