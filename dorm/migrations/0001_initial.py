# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Handlezone',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('caption', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('number', models.TextField()),
                ('level', models.IntegerField()),
                ('length', models.IntegerField()),
                ('width', models.IntegerField()),
                ('bedscount', models.IntegerField()),
                ('comfort', models.IntegerField()),
                ('bedslocked', models.IntegerField()),
                ('handlezone_id', models.ForeignKey(to='dorm.Handlezone')),
            ],
        ),
    ]
