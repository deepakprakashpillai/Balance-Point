# Generated by Django 5.1.2 on 2024-11-04 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_userassessment_bmi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userassessment',
            name='exercise_duration',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userassessment',
            name='exercise_frequency',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]