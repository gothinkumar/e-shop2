# Generated by Django 4.2.1 on 2023-07-15 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0003_computerdetail_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='computerdetail',
            old_name='img',
            new_name='image',
        ),
    ]