# Generated by Django 4.2.2 on 2023-06-28 17:31

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('social_media_link', models.CharField(blank=True, max_length=255)),
                ('social_media_choice', models.CharField(blank=True, max_length=30)),
                ('bought_items', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=list, null=True, size=None)),
                ('saved_items', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=list, null=True, size=None)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('profile_image', models.ImageField(blank=True, default=users.models.get_default_profile_image, max_length=255, null=True, upload_to=users.models.get_profile_image_filepath)),
                ('is_shop', models.BooleanField(default=False)),
                ('user_address', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('shop_name', models.CharField(blank=True, max_length=200, null=True)),
                ('verification_token', models.CharField(blank=True, max_length=255, null=True)),
                ('available_payments', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30, null=True), default=list, size=None)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SocialMedias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentsAccounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255, null=True), default=list, size=None)),
                ('account_number', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255, null=True), default=list, size=None)),
                ('payment_kind', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255, null=True), default=list, size=None)),
                ('payment_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]