# Generated by Django 5.0.7 on 2024-08-06 01:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0023_alter_address_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playground.user'),
        ),
    ]