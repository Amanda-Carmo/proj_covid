# Generated by Django 3.2.2 on 2021-05-11 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0004_profile_user_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user_name',
            new_name='nome_user',
        ),
    ]
