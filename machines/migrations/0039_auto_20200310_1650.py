# Generated by Django 3.0 on 2020-03-10 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0038_merge_20200205_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='main_channel',
            field=models.CharField(blank=True, choices=[], max_length=5, null=True, verbose_name='Канал'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='xbee_mac',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='MAC модема'),
        ),
    ]
