# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=100)),
                ('Book_name', models.CharField(max_length=10)),
                ('isbn', models.CharField(max_length=20)),
                ('desp', models.CharField(max_length=100)),
            ],
        ),
    ]
