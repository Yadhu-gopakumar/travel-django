# Generated by Django 3.2.15 on 2022-09-27 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='img',
            field=models.ImageField(upload_to='./pics'),
        ),
    ]