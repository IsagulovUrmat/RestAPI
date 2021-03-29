# Generated by Django 3.1.7 on 2021-03-19 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210319_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='bonuses',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='order_count',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]