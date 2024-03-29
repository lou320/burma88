# Generated by Django 4.2.2 on 2023-06-28 17:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('shop_id', models.IntegerField()),
                ('item_name', models.CharField(max_length=20)),
                ('shop_name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('details', models.CharField(max_length=500)),
                ('item_image1', models.ImageField(blank=True, null=True, upload_to='media/card_pic')),
                ('item_image2', models.ImageField(blank=True, null=True, upload_to='media/card_pic')),
                ('item_image3', models.ImageField(blank=True, null=True, upload_to='media/card_pic')),
                ('date_posted', models.DateTimeField(auto_now_add=True, verbose_name='card_date')),
                ('kind', models.CharField(default='nokind', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='KindOfItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('commented_at', models.DateTimeField(auto_now_add=True)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
