# Generated by Django 4.1 on 2022-11-09 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='categories', to='store.categories'),
        ),
    ]