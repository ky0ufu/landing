# Generated by Django 5.0.7 on 2024-08-17 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0004_remove_council_chairperson_council_chairperson'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presidummember',
            name='member_describtion',
        ),
        migrations.RemoveField(
            model_name='presidummember',
            name='position',
        ),
    ]
