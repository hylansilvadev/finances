# Generated by Django 5.0.7 on 2024-07-19 23:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_account_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='amount',
            new_name='balance',
        ),
    ]
