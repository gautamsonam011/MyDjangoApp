# Generated by Django 5.1.4 on 2024-12-12 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MDA', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Member',
            new_name='User',
        ),
    ]
