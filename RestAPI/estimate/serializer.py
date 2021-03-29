from rest_framework import serializers
from .models import Rate

class RateSerializer(serializers.ModelSerializer):

    star = serializers.IntegerField(min_value=0, max_value=5)

    class Meta:
        model = Rate
        fields = ['id', 'worker', 'start', 'date_created', 'profile']


class RateCreateSerializer(serializers.Serializer):

    star = serializers.IntegerField(min_value=0, max_value=5)
