# Generated by Django 5.0.2 on 2024-10-18 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pc_app', '0032_alter_services_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='name',
        ),
    ]
