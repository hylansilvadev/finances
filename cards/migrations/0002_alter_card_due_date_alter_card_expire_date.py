# Generated by Django 5.0.7 on 2024-07-17 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='due_date',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='card',
            name='expire_date',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
