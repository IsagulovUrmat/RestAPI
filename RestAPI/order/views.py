from django.shortcuts import render
from rest_framework.response import Response
from .serializer import *
from rest_framework import views, status
from .models import Table
from .services import use_promo, get_pay
from django.utils import timezone


class OrderView(views.APIView):

    def get(self, request, *args, **kwargs):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders,many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # user = serializer.data.get('user')
            # count_orders(user)
            order_id = serializer.data.get('id')
            total_sum = serializer.data.get('total_sum')
            get_pay(order_id)
            # count_bonuses(user,total_sum)
            return Response({"data":"OK!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


class RestaurantProfileView(views.APIView):

    def get(self, request, *args, **kwargs):
        profile = RestaurantProfile.objects.get(user=request.user)
        serializer = RestaurantProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        profile = RestaurantProfile.objects.get(user=request.user)
        serializer = RestaurantProfileSerializer(profile,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"UPDATE SUCCESSFULL!"})
        return Response(serializer.errors)

    def delete(self, request, *args, **kwargs):
        profile = RestaurantProfile.objects.get(user=request.user)
        profile.delete()
        return Response({"data": "OK"})

class TableView(views.APIView):

    def get(self, request, *args, **kwargs):
        table = Table.objects.all()
        serializer = TableSerializer(table, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = TableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': 'OK!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


class TableDetailView(views.APIView):

    def get(self, request, *args, **kwargs):
        try:
            table = Table.objects.get(id=kwargs['table_id'])
        except Table.DoesNotExist:
            return Response({'data': 'Table not found!'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TableDetailSerializer(table)
        return Response(serializer.data)


class ModifyOrderView(views.APIView):

    def put(self, request, *args, **kwargs):

        order = Order.objects.get(id=kwargs['order_id'])
        order_minute, order_hour = order.date_created.minute, order.date_created.hour * 60
        current_minute, current_hour = timezone.now().minute, timezone.now().hour * 60
        order_time = order_minute + order_hour
        current_time = current_minute + current_hour
        abs_value = abs(order_time - current_time)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            if abs_value <= 5 and order.status == 'in_process':
                serializer.save()
                return Response({"data": 'order updated successfully'})
            return Response({"data": f"Time is up or order is {order.status}"})
        return Response(serializer.errors)


    def delete(self, request, *args, **kwargs):

        order = Order.objects.get(id=kwargs['order_id'])
        order_minute, order_hour = order.date_created.minute, order.date_created.hour * 60
        current_minute, current_hour = timezone.now().minute, timezone.now().hour * 60
        order_time = order_minute + order_hour
        current_time = current_minute + current_hour
        abs_value = abs(order_time - current_time)

        if abs_value <= 5 and order.status == 'in_process':
            order.delete()
            return Response("Order is cancelled!")
        return Response(f"Time is up or order is {order.status}")








