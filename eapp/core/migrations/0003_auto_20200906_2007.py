# Generated by Django 3.1.1 on 2020-09-06 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200906_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(max_length=1000, upload_to=''),
        ),
    ]
