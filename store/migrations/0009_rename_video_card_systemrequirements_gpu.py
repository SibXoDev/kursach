# Generated by Django 4.1 on 2022-09-10 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_remove_systemrequirements_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='systemrequirements',
            old_name='video_card',
            new_name='gpu',
        ),
    ]
