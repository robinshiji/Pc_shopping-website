# Generated by Django 5.0.2 on 2024-10-15 15:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pc_app', '0007_remove_cart_content_type_remove_cart_object_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='prebuilt',
        ),
        migrations.AlterField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pc_app.product'),
        ),
    ]
