# Generated by Django 5.0.2 on 2024-10-17 15:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pc_app', '0020_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='items',
        ),
        migrations.RemoveField(
            model_name='order',
            name='ordered_at',
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(default='pending', max_length=20),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='pc_app.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pc_app.product')),
            ],
        ),
    ]