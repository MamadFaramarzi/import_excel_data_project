# Generated by Django 5.0.7 on 2024-07-11 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_data', '0006_remove_data_total_price_remove_data_unit_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
