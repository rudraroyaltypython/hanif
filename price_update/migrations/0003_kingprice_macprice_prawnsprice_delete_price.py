# Generated by Django 5.1.3 on 2024-11-21 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price_update', '0002_alter_price_retail_alter_price_wholesale'),
    ]

    operations = [
        migrations.CreateModel(
            name='KingPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wholesale', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MacPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wholesale', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PrawnsPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wholesale', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Price',
        ),
    ]
