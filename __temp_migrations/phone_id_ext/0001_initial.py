# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-08-31 11:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import otree.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkedSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='otree.Session')),
            ],
        ),
        migrations.CreateModel(
            name='PhoneRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_id', otree.db.models.IntegerField(null=True)),
                ('taken', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('linked_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phonerecords', to='phone_id_ext.LinkedSession')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='otree.Participant')),
            ],
        ),
    ]