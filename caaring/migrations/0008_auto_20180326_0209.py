# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-25 20:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caaring', '0007_auto_20180326_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='approval_status',
            field=models.CharField(choices=[('Approved', 'APPROVED'), ('Declined', 'DECLINED'), ('Requested', 'REQUESTED')], max_length=10),
        ),
    ]
