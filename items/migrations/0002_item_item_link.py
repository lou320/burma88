# Generated by Django 4.2.3 on 2023-07-23 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_link',
            field=models.CharField(default=None, max_length=300),
        ),
    ]
