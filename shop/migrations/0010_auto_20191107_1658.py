# Generated by Django 2.0.13 on 2019-11-07 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20191107_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='categories',
            field=models.ManyToManyField(default=None, related_name='catalogs', to='shop.Categories'),
        ),
    ]
