# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0033_seats'),
    ]

    operations = [
        migrations.AddField(
            model_name='seats',
            name='seats',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
