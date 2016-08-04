# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-03 22:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20160803_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(to='books.Author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ManyToManyField(to='books.Publisher'),
        ),
    ]
