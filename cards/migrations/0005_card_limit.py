# Generated by Django 5.0.7 on 2024-07-17 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0004_alter_card_card_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='limit',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
