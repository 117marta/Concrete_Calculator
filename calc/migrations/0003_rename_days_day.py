# Generated by Django 3.2.10 on 2021-12-07 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0002_days_person'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Days',
            new_name='Day',
        ),
    ]
