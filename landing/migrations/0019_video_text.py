# Generated by Django 5.0.7 on 2024-08-01 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0018_remove_photo_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='text',
            field=models.TextField(default='text'),
        ),
    ]
