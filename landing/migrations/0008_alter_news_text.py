# Generated by Django 5.0.7 on 2024-08-22 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0007_alter_news_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='text',
            field=models.TextField(default='Tекст', verbose_name='Текст новости'),
        ),
    ]
