# Generated by Django 3.2.10 on 2021-12-09 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0005_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='legal_name',
            field=models.CharField(max_length=150, null=True, verbose_name='Imię i nazwisko'),
        ),
    ]
