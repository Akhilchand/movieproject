# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0024_auto_20170314_1720'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seat_available', models.IntegerField(null=True, blank=True)),
                ('seat_num', models.CharField(max_length=1000, null=True, blank=True)),
                ('total_seats', models.CharField(max_length=1000, null=True, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='booking_info',
            name='seat_available',
        ),
        migrations.RemoveField(
            model_name='booking_info',
            name='seat_num',
        ),
        migrations.RemoveField(
            model_name='booking_info',
            name='total_seats',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.DecimalField(default=0, null=True, max_digits=10, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='seats',
            name='show',
            field=models.ForeignKey(to='movieapp.Booking_info'),
        ),
    ]
