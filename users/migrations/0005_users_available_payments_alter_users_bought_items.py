# Generated by Django 4.2.2 on 2023-06-29 02:15

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_users_bought_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='available_payments',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(), blank=True, default=list, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='users',
            name='bought_items',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=list, null=True, size=None),
        ),
    ]
