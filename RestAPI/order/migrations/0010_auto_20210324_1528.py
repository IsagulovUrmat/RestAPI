# Generated by Django 3.1.7 on 2021-03-24 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_promocode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promocode',
            name='sale',
            field=models.FloatField(default=0.1),
        ),
    ]