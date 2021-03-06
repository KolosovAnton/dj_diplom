# Generated by Django 2.0.13 on 2019-11-08 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_auto_20191108_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='short_name',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='categories',
            name='short_name',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='short_name',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
