# Generated by Django 5.1.3 on 2024-11-26 17:41

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]