# Generated by Django 5.1.3 on 2024-11-21 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price_update', '0004_alter_kingprice_wholesale_alter_macprice_wholesale_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kingprice',
            name='wholesale',
            field=models.CharField(max_length=50, verbose_name='King Fish (सुरमई) Wholesale Price per kg'),
        ),
        migrations.AlterField(
            model_name='macprice',
            name='wholesale',
            field=models.CharField(max_length=50, verbose_name='Mackerel (बांगडा) Wholesale Price per kg'),
        ),
        migrations.AlterField(
            model_name='prawnsprice',
            name='wholesale',
            field=models.CharField(max_length=50, verbose_name='Prawns (कोळंबी) Wholesale Price per kg'),
        ),
    ]