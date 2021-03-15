from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):

    status = serializers.CharField(read_only=True)
    total_price = serializers.IntegerField(read_only=True)
    total_sum = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id','meal','quantity','table', 'date_created','status', 'total_price']


    def get_total_sum(self, obj):
        total_sum = obj.meal.price * obj.quantity
        obj.total_price = total_sum
        obj.save()
        return total_sum