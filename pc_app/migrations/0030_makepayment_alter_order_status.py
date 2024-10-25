# Generated by Django 5.0.2 on 2024-10-18 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pc_app', '0029_alter_order_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='makepayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardnumber', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('cvv', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Shipped', 'Shipped'), ('out for delivery', 'Out for delivery'), ('delivered', 'Delivered'), ('Product Returned', 'Product Returned')], default='Pending', max_length=20),
        ),
    ]
