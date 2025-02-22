# Generated by Django 5.0.7 on 2024-07-17 02:43

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('final_number', models.IntegerField()),
                ('due_date', models.DateField()),
                ('expire_date', models.DateField()),
                ('brand', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cards.brand')),
            ],
        ),
    ]
