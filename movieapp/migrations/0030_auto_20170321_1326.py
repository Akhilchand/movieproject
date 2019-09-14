# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0029_auto_20170321_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='seat_status',
            field=models.CharField(max_length=50, choices=[(b'S', b'Selected'), (b'N', b'Not_Selected')]),
        ),
    ]
