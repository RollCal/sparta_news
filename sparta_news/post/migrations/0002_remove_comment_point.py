# Generated by Django 4.2.11 on 2024-05-09 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='point',
        ),
    ]
