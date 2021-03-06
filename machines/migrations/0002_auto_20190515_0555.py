# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-15 05:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=30, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f')),
                ('first_name', models.CharField(max_length=30, verbose_name='\u0418\u043c\u044f')),
                ('second_name', models.CharField(max_length=30, verbose_name='\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e')),
                ('login', models.CharField(max_length=30, verbose_name='\u041b\u043e\u0433\u0438\u043d')),
                ('phone', models.CharField(max_length=10, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('role', models.CharField(choices=[('administrator', '\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440'), ('operator', '\u0420\u0430\u0431\u043e\u0447\u0438\u0439'), ('master', '\u041c\u0430\u0441\u0442\u0435\u0440'), ('manager', '\u0420\u0443\u043a\u043e\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c')], max_length=20, verbose_name='\u0420\u043e\u043b\u044c')),
            ],
        ),
        migrations.RenameModel(
            old_name='Reasons',
            new_name='Reason',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
