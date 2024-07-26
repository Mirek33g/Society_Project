# Generated by Django 5.0.7 on 2024-07-25 20:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=255)),
                ('registered_at', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('post_type', models.CharField(choices=[('P', 'Positive'), ('N', 'Negative')], default='P', max_length=1)),
                ('placed_at', models.DateTimeField()),
                ('user_post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='playground.user')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('user_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playground.user')),
            ],
        ),
    ]
