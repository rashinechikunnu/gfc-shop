# Generated by Django 5.0.7 on 2024-09-04 05:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_payment_product_order_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_me', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('replay', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.customer')),
            ],
        ),
    ]
