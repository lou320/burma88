# Generated by Django 4.2.3 on 2023-10-22 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0012_alter_item_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='gram',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
