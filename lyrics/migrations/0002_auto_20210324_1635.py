# Generated by Django 3.1.7 on 2021-03-24 16:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('lyrics', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bridge',
            old_name='brige',
            new_name='bridge',
        ),
        migrations.AddField(
            model_name='lyric',
            name='unique_num',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
