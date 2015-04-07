# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('picture', models.CharField(max_length=500)),
                ('rating', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('coupons', models.ManyToManyField(to='home.Coupon')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
