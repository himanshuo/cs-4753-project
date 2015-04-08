# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_coupon_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='products_seen',
            field=models.ManyToManyField(to='home.Product'),
            preserve_default=True,
        ),
    ]
