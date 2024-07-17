# Generated by Django 5.0.7 on 2024-07-17 12:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bills',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='bills',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2024, 7, 17, 9, 3, 10, 793711)),
        ),
        migrations.AddField(
            model_name='bills',
            name='issue_date',
            field=models.DateField(default=datetime.datetime(2024, 7, 17, 9, 3, 10, 793698)),
        ),
        migrations.AddField(
            model_name='bills',
            name='payment_type',
            field=models.CharField(choices=[('CC', 'Credit Card'), ('DC', 'Debit Card'), ('MO', 'Money')], default='MO', max_length=2),
        ),
        migrations.AddField(
            model_name='bills',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]
