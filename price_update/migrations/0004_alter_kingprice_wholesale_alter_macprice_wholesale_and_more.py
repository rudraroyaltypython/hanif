# Generated by Django 5.1.3 on 2024-11-21 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price_update', '0003_kingprice_macprice_prawnsprice_delete_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kingprice',
            name='wholesale',
            field=models.CharField(max_length=50, verbose_name='Wholesale Price per kg'),
        ),
        migrations.AlterField(
            model_name='macprice',
            name='wholesale',
            field=models.CharField(max_length=50, verbose_name='Wholesale Price per kg'),
        ),
        migrations.AlterField(
            model_name='prawnsprice',
            name='wholesale',
            field=models.CharField(max_length=50, verbose_name='Wholesale Price per kg'),
        ),
    ]
