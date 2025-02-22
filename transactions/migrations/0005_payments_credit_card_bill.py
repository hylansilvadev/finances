# Generated by Django 5.0.7 on 2024-07-21 11:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0011_alter_bills_category_creditcardbill'),
        ('transactions', '0004_alter_payments_transaction_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='credit_card_bill',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='bills.creditcardbill'),
        ),
    ]
