# Generated by Django 5.1.2 on 2024-11-04 08:57

import django.db.models.deletion
import multiselectfield.db.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DiaryLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('mood_descriptors', multiselectfield.db.fields.MultiSelectField(choices=[('productive', 'Productive'), ('energetic', 'Energetic'), ('happy', 'Happy'), ('motivated', 'Motivated'), ('content', 'Content'), ('relaxed', 'Relaxed'), ('accomplished', 'Accomplished'), ('tired', 'Tired'), ('stressed', 'Stressed'), ('anxious', 'Anxious')], max_length=88)),
                ('emotional_rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)])),
                ('notes', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='diary_logs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
