from django.db import models

class Meal(models.Model):

    portions = (
        ('0.7', '0.7'),
        ('1', '1')
    )

    name = models.CharField(max_length=50, verbose_name='Изображение')
    description = models.CharField(max_length=200, verbose_name='Состав')
    price = models.PositiveIntegerField(verbose_name='Цена')
    portion = models.CharField(choices=portions, max_length=50, verbose_name='Порция')
    image = models.ImageField(blank=True, null=True, verbose_name='Изображение')

    def __str__(self):
        return self.name


class Category(models.Model):


