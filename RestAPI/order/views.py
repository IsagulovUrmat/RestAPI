from django.shortcuts import render
from rest_framework.response import Response
from .serializer import *
from rest_framework import views, status


class OrderView(views.APIView):

    def get(self, request, *args, **kwargs):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders,many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":"OK!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)