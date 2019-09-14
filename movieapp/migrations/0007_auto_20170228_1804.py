# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0006_songs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='songs',
            old_name='tarck1',
            new_name='track1',
        ),
    ]
