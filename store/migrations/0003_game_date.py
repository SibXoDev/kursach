# Generated by Django 4.1 on 2022-09-10 08:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_game_media_alter_game_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='date',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2022, 9, 10, 8, 22, 14, 327671, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
