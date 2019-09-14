# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0027_auto_20170321_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='movie',
            field=models.ForeignKey(default=1, to='movieapp.Movie'),
            preserve_default=False,
        ),
    ]
