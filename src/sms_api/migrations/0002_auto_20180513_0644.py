# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-13 06:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='smsinfo',
            options={'ordering': ['-sent_date']},
        ),
    ]
