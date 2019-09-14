# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0030_auto_20170321_1326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seat',
            name='seat_status',
        ),
    ]
