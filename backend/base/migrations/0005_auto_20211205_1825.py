# Generated by Django 3.2.9 on 2021-12-05 18:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0004_order_orderitem_shippingaddress'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reviews',
            new_name='Review',
        ),
        migrations.RemoveField(
            model_name='product',
            name='numReviews',
        ),
        migrations.AddField(
            model_name='product',
            name='numReview',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
