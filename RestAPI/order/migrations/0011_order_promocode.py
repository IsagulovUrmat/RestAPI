# Generated by Django 3.1.7 on 2021-03-24 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_auto_20210324_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='promocode',
            field=models.CharField(blank=True, default='1', max_length=10, null=True),
        ),
    ]
