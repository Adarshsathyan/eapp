# Generated by Django 3.1.1 on 2020-09-16 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200913_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='phonenumber',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
