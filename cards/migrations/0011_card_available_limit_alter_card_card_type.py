# Generated by Django 5.0.7 on 2024-07-21 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0010_alter_card_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='available_limit',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='card',
            name='card_type',
            field=models.CharField(choices=[('DE', 'Debit'), ('CR', 'Credit'), ('BF', 'Both'), ('BO', 'Benefits')], default='BO', max_length=2),
        ),
    ]
