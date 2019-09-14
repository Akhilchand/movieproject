# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0004_userdetail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moviedetail',
            old_name='movie_id',
            new_name='movie',
        ),
    ]
