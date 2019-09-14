# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0026_auto_20170321_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_sel',
            name='booking',
            field=models.ForeignKey(to='movieapp.Seat'),
        ),
    ]
