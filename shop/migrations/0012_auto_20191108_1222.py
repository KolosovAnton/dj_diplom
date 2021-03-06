# Generated by Django 2.0.13 on 2019-11-08 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20191107_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='short_name',
            field=models.CharField(default='1', max_length=15),
        ),
        migrations.AlterField(
            model_name='categories',
            name='catalog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Catalog'),
        ),
    ]
