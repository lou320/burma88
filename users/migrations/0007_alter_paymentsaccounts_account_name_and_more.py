# Generated by Django 4.2.2 on 2023-06-29 02:34

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_users_available_payments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentsaccounts',
            name='account_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='paymentsaccounts',
            name='account_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='paymentsaccounts',
            name='payment_kind',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='available_payments',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(), blank=True, default=list, null=True, size=None),
        ),
    ]
