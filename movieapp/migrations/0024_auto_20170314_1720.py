# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0023_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
