# Generated by Django 4.1.3 on 2022-11-03 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_rename_author_product_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
