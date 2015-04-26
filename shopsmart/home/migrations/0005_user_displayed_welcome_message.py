# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='displayed_welcome_message',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
