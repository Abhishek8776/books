# Generated by Django 5.0 on 2023-12-12 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookmodal',
            old_name='auther',
            new_name='author',
        ),
    ]