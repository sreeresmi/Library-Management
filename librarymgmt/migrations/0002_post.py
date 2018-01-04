# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('librarymgmt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=250)),
                ('age', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=500)),
                ('Born_in', models.CharField(max_length=250)),
                ('abt_author', models.CharField(max_length=1000)),
            ],
        ),
    ]
