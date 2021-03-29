# Generated by Django 3.1.7 on 2021-03-26 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0006_card_status'),
        ('order', '0017_auto_20210324_2043'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star', models.PositiveIntegerField(default=None, null=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.userprofile')),
                ('worker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.restaurantprofile')),
            ],
        ),
    ]