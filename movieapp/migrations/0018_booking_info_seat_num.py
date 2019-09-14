# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0017_user_sel_selected_seats'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking_info',
            name='seat_num',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]
