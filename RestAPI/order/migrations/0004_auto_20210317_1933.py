# Generated by Django 3.1.7 on 2021-03-17 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20210317_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantprofile',
            name='date_start',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='restaurantprofile',
            name='schedule',
            field=models.CharField(choices=[('2/2', '2/2'), ('5/2', '5/2')], max_length=50),
        ),
    ]