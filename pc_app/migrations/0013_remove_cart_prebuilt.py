# Generated by Django 5.0.2 on 2024-10-16 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pc_app', '0012_alter_cart_prebuilt_alter_cart_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='prebuilt',
        ),
    ]
