# Generated by Django 5.0.7 on 2024-07-17 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0005_alter_bills_due_date_alter_bills_issue_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
            ],
        ),
    ]
