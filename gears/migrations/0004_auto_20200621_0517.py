# Generated by Django 3.0.7 on 2020-06-21 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gears', '0003_auto_20200620_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gears',
            name='description',
            field=models.TextField(default='No Details'),
        ),
    ]