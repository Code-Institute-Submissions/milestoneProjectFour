# Generated by Django 3.1.5 on 2021-01-26 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210125_2236'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image_1',
            new_name='image1',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='image_url_1',
            new_name='image1_url',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='image_2',
            new_name='image2',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='image_url_2',
            new_name='image2_url',
        ),
    ]
