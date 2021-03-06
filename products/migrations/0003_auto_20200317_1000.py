# Generated by Django 3.0.4 on 2020-03-17 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0004_auto_20200315_2052'),
        ('products', '0002_remove_product_order_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Product_order',
        ),
    ]
