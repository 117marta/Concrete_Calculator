# Generated by Django 3.2.10 on 2021-12-11 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0006_list_legal_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='phone',
            field=models.IntegerField(null=True, verbose_name='Telefon'),
        ),
    ]
