# Generated by Django 4.0 on 2021-12-22 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='fname',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='lname',
        ),
    ]