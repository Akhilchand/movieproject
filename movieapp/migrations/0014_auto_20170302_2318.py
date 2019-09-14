# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0013_auto_20170302_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking_info',
            name='seat_available',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
