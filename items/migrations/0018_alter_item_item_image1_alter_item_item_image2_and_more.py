# Generated by Django 4.2.3 on 2023-10-26 04:53

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0017_alter_item_item_image1_alter_item_item_image2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image1',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image_1'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_image2',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image_2'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_image3',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image_3'),
        ),
    ]
