# Generated by Django 3.2.10 on 2021-12-09 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0004_rename_descriptions_person_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shape', models.CharField(max_length=50, verbose_name='Kształt')),
                ('volume', models.FloatField(null=True, verbose_name='Objętość')),
                ('concrete', models.CharField(max_length=50, verbose_name='Beton')),
                ('use_of_concrete', models.CharField(max_length=100, verbose_name='Zastosowanie')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Utworzono')),
                ('comment', models.TextField(null=True, verbose_name='Komentarz')),
            ],
        ),
    ]
