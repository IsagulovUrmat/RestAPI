# Generated by Django 3.1.7 on 2021-03-24 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0002_auto_20210315_1924'),
        ('order', '0012_auto_20210324_1809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='meal',
        ),
        migrations.AddField(
            model_name='order',
            name='meal',
            field=models.ManyToManyField(to='rest.Meal'),
        ),
    ]
