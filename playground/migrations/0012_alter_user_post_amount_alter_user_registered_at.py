# Generated by Django 5.0.7 on 2024-08-02 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0011_alter_user_post_amount_alter_user_registered_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='post_amount',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='registered_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]