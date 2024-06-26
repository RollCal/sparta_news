# Generated by Django 4.2.11 on 2024-05-09 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('search_engine', '0002_document_embedding'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpartanewsDocument',
            fields=[
                ('document_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='search_engine.document')),
            ],
            bases=('search_engine.document',),
        ),
    ]
