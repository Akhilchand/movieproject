# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0016_auto_20170303_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_sel',
            name='selected_seats',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]
