# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-03 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyTUID', '0003_auto_20170514_1146'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tuiduser',
            options={'verbose_name': 'TUID Benutzer', 'verbose_name_plural': 'TUID Users'},
        ),
        migrations.AlterField(
            model_name='tuiduser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-Mail'),
        ),
    ]
