# Generated by Django 4.1.3 on 2022-11-12 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitems',
            name='price_per_unit',
            field=models.FloatField(default=0),
        ),
    ]
