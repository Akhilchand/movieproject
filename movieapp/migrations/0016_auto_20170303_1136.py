# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0015_auto_20170303_1136'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_sel',
            old_name='seats_avail',
            new_name='seats',
        ),
    ]
