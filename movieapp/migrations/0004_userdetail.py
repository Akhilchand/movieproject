# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0003_auto_20170224_1322'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, null=True, blank=True)),
                ('first_name', models.CharField(max_length=30, null=True, blank=True)),
                ('last_name', models.CharField(max_length=30, null=True, blank=True)),
                ('address', models.CharField(max_length=50, null=True, blank=True)),
                ('mobile', models.CharField(max_length=30, null=True, blank=True)),
                ('mail', models.EmailField(max_length=50, null=True, blank=True)),
            ],
        ),
    ]
