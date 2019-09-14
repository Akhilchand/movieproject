# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0019_auto_20170307_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking_info',
            name='seat_num',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
    ]
