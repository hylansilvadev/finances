# Generated by Django 5.0.7 on 2024-07-17 19:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0008_card_created_at_card_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='created_at',
            field=models.DateField(default=datetime.datetime.now, editable=False),
        ),
        migrations.AlterField(
            model_name='card',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]
