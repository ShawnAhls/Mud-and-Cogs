# Generated by Django 3.0.7 on 2020-06-21 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brakes', '0002_auto_20200621_0517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brakes',
            name='price',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=6),
        ),
    ]