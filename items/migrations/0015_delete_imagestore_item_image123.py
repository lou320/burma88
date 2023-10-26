# Generated by Django 4.2.3 on 2023-10-26 04:20

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0014_imagestore'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ImageStore',
        ),
        migrations.AddField(
            model_name='item',
            name='image123',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image'),
        ),
    ]
