# Generated by Django 4.2.9 on 2024-01-24 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Choic',
            new_name='Choice',
        ),
    ]
