# Generated by Django 5.0.2 on 2024-10-15 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pc_app', '0003_remove_cart_prebuilt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='product',
            field=models.CharField(max_length=255),
        ),
    ]
