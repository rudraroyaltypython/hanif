# Generated by Django 5.1.1 on 2024-10-03 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wholesale', models.DecimalField(decimal_places=2, max_digits=5)),
                ('retail', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
