# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movieapp', '0034_seats_seats'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seats',
            old_name='seats',
            new_name='seat',
        ),
        migrations.AddField(
            model_name='seats',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='seats',
            name='seat_status',
            field=models.BooleanField(default=True),
        ),
    ]
