# Generated by Django 5.1.4 on 2025-02-06 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_coupon_order_coupon_code_order_discount_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='coupon_code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='discount_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
