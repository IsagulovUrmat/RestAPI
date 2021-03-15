from rest_framework import serializers
from .models import *

class MealSerializerHard(serializers.Serializer):

    portions = (
        ('0.7', '0.7'),
        ('1', '1')
    )

    name = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=50)
    price = serializers.IntegerField(min_value=0)
    portion = serializers.ChoiceField(choices=portions)


class MealSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meal
        fields = '__all__'
