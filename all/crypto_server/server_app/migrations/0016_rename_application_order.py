# Generated by Django 4.1.3 on 2023-01-12 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server_app', '0015_remove_application_nickname_application_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Application',
            new_name='Order',
        ),
    ]
