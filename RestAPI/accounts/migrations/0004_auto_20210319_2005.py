# Generated by Django 3.1.7 on 2021-03-19 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210319_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='accounts.userprofile'),
        ),
    ]
