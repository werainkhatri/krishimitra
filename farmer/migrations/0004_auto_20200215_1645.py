# Generated by Django 3.0.3 on 2020-02-15 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0003_auto_20200215_1538'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='price_per_kg',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_type',
            new_name='type',
        ),
    ]