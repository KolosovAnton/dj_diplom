# Generated by Django 2.1.1 on 2019-11-12 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_remove_article_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(upload_to='media'),
        ),
    ]
