# Generated by Django 2.1.1 on 2019-11-27 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='quantity_item',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Количество товаров'),
        ),
    ]