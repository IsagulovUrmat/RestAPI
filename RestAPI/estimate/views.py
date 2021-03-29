from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from order.serializer import RestaurantProfileSerializer
from order.models import Order
from order.serializer import OrderSerializer
from .serializer import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class RateView(APIView):

    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        try:
            profile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            try:
                profile = RestaurantProfile.objects.get(user=request.user)
            except RestaurantProfile.DoesNotExist:
                return Response({"data": "Please log in!"})

        if isinstance(profile, UserProfile):
            orders = Order.objects.filter(userprofile=profile)
            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data)


        return Response({"data": "YOU SHALL NOT PASS!"})


class RateWorkerView(APIView):

    def get(self, request, *args, **kwargs):
        worker = RestaurantProfile.objects.get(id=kwargs['worker_id'])
        serializer = RestaurantProfileSerializer(worker)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):

        serializer = RateCreateSerializer(data=request.data)
        worker = RestaurantProfile.objects.get(id=kwargs['worker_id'])
        userprofile = request.user.userprofile

        if serializer.is_valid():

            Rate.objects.create(star=serializer.data.get('star'), worker=worker, user=userprofile)
            return Response({"DATA": "OK!"})
        return Response(serializer.errors)

