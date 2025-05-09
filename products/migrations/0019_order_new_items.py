# Generated by Django 5.1.4 on 2025-03-01 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='new_items',
            field=models.ManyToManyField(related_name='new_order_items', through='products.OrderItem', to='products.product'),
        ),
    ]
