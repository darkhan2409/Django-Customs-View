# Generated by Django 4.2.6 on 2023-10-25 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_rename_songs_song'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='part_text',
            field=models.TextField(null=True),
        ),
    ]
