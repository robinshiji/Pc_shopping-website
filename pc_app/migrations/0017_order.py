# Generated by Django 5.0.2 on 2024-10-16 10:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pc_app', '0016_delete_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('shipped', 'Shipped'), ('delivered', 'Delivered')], default='pending', max_length=10)),
                ('comp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pc_app.company')),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pc_app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pc_app.user')),
            ],
        ),
    ]