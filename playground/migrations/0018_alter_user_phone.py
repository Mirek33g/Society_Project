# Generated by Django 5.0.7 on 2024-08-05 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0017_alter_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(blank=True, max_length=255, null=True),
        ),
    ]