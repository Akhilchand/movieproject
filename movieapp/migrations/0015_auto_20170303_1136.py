# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0014_auto_20170302_2318'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_sel',
            old_name='seats',
            new_name='booking',
        ),
    ]
