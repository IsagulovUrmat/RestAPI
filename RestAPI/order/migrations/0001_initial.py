# Generated by Django 3.1.7 on 2021-03-15 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rest', '0002_auto_20210315_1924'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('total_price', models.PositiveIntegerField(default=0)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('table', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('Ready', 'Ready'), ('in_process', 'in_process')], default='in_process', max_length=20)),
                ('meal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rest.meal')),
            ],
        ),
    ]
