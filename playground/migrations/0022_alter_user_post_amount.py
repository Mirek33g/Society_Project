# Generated by Django 5.0.7 on 2024-08-06 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0021_user_user_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='post_amount',
            field=models.IntegerField(null=True),
        ),
    ]
