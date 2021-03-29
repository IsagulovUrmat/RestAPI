from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .services import use_promo
from .models import Order, RestaurantProfile, Table, MealToOrder
from accounts.services import *
from django.db import IntegrityError

class MTOSerializer(serializers.ModelSerializer):

    class Meta:
        model = MealToOrder
        fields = ['id', 'meal', 'quantity']

class OrderSerializer(serializers.ModelSerializer):

    status = serializers.CharField(read_only=True)
    total_price = serializers.IntegerField(read_only=True)
    total_sum = serializers.SerializerMethodField()
    # promo = serializers.SerializerMethodField()
    # MTO = MTOSerializer(many=True)


    class Meta:
        model = Order
        fields = ['id','table', 'date_created', 'status', 'total_price',
                  'userprofile', 'worker', 'payment_type', 'promocode', 'total_sum']

    # def create(self, validated_data):
    #     MTO_data = validated_data.pop('MTO')
    #     userprofile = validated_data.pop('userprofile')
    #     worker = validated_data.pop('worker')
    #     if userprofile is not None and worker is not None:
    #         order = Order.objects.create(worker=worker, userprofile=userprofile, **validated_data)
    #     else:
    #         if userprofile is None:
    #             order = Order.objects.create(worker=worker, **validated_data)
    #         else:
    #             order = Order.objects.create(userprofile=userprofile, **validated_data)
    #     for meal in MTO_data:
    #         MealToOrder.objects.create(order=order, **meal)
    #     return order


    def get_total_sum(self, obj):
        total_sum = 0
        for mto in obj.MTO.all():
            total_sum += mto.meal.price * mto.quantity
        obj.total_price = total_sum
        obj.save()
        return total_sum



    # def get_pay(self, obj):
    #     card = obj.user.userprofile.cards.filter(status='default')[0]
    #     if obj.payment_type == 'card' and obj.status != 'closed':
    #         try:
    #             card.balance -= obj.total_price
    #             card.save()
    #             obj.status = 'closed'
    #             obj.save()
    #         except IntegrityError:
    #             raise ValidationError("Not enough money!")



class TableSerializer(serializers.ModelSerializer):

    class Meta:
        model = Table
        fields = ['id', 'area', 'status']


class TableDetailSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True)

    class Meta:
        model = Table
        fields = ['id', 'area', 'status', 'orders']



class RestaurantProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = RestaurantProfile
        fields = ['id', 'full_name', 'age', 'date_start', 'date_end',
                  'salary', 'schedule','user'
                  ]



