# Generated by Django 5.1.4 on 2025-03-14 13:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0011_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2025, 3, 14, 16, 49, 9, 298105)),
        ),
    ]
