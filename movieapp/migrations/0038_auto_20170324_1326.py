# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0037_bookingtransactions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookingtransactions',
            old_name='show',
            new_name='seat',
        ),
    ]
