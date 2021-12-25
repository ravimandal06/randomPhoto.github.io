# Generated by Django 4.0 on 2021-12-22 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=122)),
                ('lname', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('desc', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
