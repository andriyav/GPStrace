# Generated by Django 4.0.3 on 2022-04-11 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='complite',
            new_name='complete',
        ),
    ]
