# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0038_auto_20170324_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingtransactions',
            name='seat',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
