# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0010_auto_20170302_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_sel',
            name='seats_avail',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
