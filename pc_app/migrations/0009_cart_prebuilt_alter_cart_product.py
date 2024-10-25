# Generated by Django 5.0.2 on 2024-10-15 15:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pc_app', '0008_remove_cart_prebuilt_alter_cart_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='prebuilt',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pc_app.prebuilt'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pc_app.product'),
        ),
    ]
