# Generated by Django 4.2.2 on 2023-06-29 02:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_users_available_payments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='available_payments',
        ),
    ]
