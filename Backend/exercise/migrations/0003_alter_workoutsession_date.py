# Generated by Django 5.1.2 on 2024-11-09 10:21

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workoutsession',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
