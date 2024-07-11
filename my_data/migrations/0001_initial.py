# Generated by Django 5.0.7 on 2024-07-10 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('product', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=350)),
                ('quantity', models.PositiveIntegerField()),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date_time', models.DateTimeField()),
            ],
        ),
    ]
