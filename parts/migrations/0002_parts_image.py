# Generated by Django 3.0.7 on 2020-07-23 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parts',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]