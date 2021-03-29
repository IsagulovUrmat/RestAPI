from rest_framework import serializers, status
from rest_framework.response import Response

from .models import *


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = ['id', 'holder_name', 'number', 'date', 'code', 'balance', 'profile']


class CardCreateSerialier(serializers.Serializer):
    number = serializers.IntegerField()
    date = serializers.DateField()
    holder_name = serializers.CharField(max_length=20)
    code = serializers.IntegerField(min_value=100,max_value=999)





class UserProfileSerializer(serializers.ModelSerializer):

    cards = CardSerializer(many=True)
    bonuses = serializers.IntegerField(read_only=True)
    order_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'full_name', 'street', 'house', 'phone', 'bonuses', 'order_count', 'email',
                  'cards']



