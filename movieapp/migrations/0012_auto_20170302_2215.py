# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0011_user_sel_seats_avail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_sel',
            name='seats_avail',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
