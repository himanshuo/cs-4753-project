# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('picture', models.CharField(max_length=500)),
                ('rating', models.IntegerField()),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('price_discount', models.DecimalField(max_digits=10, decimal_places=2)),
                ('coupons', models.ManyToManyField(to='home.Coupon')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('email', models.EmailField(max_length=75, unique=True)),
                ('products_seen', models.ManyToManyField(to='home.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
