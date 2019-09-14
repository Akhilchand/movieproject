# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0021_auto_20170310_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking_info',
            name='movie',
            field=models.ForeignKey(default=1, to='movieapp.Movie'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='moviedetail',
            name='movie',
            field=models.ForeignKey(default=1, to='movieapp.Movie'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='songs',
            name='movie',
            field=models.ForeignKey(default=1, to='movieapp.Movie'),
            preserve_default=False,
        ),
    ]
