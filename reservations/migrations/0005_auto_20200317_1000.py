# Generated by Django 3.0.4 on 2020-03-17 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200317_1000'),
        ('reservations', '0004_auto_20200315_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='res',
            name='products',
            field=models.ManyToManyField(to='products.Product'),
        ),
    ]
