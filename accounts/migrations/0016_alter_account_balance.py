# Generated by Django 5.0.7 on 2024-07-20 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_alter_account_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='balance',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, editable=False, max_digits=10),
        ),
    ]
