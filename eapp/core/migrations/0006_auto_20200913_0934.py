# Generated by Django 3.1.1 on 2020-09-13 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/assets/img'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/assets/img'),
        ),
    ]
