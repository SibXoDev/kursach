# Generated by Django 4.1 on 2022-09-11 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_rename_video_card_systemrequirements_gpu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='systemrequirements',
            name='name',
        ),
    ]
