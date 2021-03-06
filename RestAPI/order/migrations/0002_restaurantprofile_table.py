# Generated by Django 3.1.7 on 2021-03-16 17:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(choices=[('Main Hall', 'Main Hall'), ('Outdoor', 'Outdoor'), ('VIP', 'VIP')], default='Main Hall', max_length=20)),
                ('status', models.CharField(choices=[('Reserved', 'Reserved'), ('Empty', 'Empty')], default='Empty', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='RestaurantProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=20)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('salary', models.PositiveIntegerField(default=0)),
                ('schedule', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
