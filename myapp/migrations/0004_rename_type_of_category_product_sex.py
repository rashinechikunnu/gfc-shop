# Generated by Django 5.0.7 on 2024-08-14 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='type_of_category',
            new_name='sex',
        ),
    ]
