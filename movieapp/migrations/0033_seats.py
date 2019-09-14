# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0032_auto_20170321_1358'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seat_status', models.CharField(max_length=50, choices=[(b'S', b'Selected'), (b'V', b'Not Selected')])),
                ('show', models.ForeignKey(to='movieapp.Booking_info')),
            ],
        ),
    ]
