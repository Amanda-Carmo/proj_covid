# Generated by Django 3.2.2 on 2021-05-11 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0003_auto_20210506_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_name',
            field=models.TextField(default='', max_length=20, unique=True),
        ),
    ]
