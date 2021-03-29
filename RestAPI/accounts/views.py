from django.shortcuts import render
from rest_framework.response import Response
from .serializer import *
from rest_framework import views, status
from .models import *

class UserProfileView(views.APIView):

    def get(self, request, *args, **kwargs):
        try:
            profile = UserProfile.objects.get(user=request.user)
        except TypeError:
            return Response({"data": "Profile not found!"}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        try:
            profile = UserProfile.objects.get(user=request.user)
        except TypeError:
            return Response({"data": "Profile not found!"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CardCreateSerialier(data=request.data)
        if serializer.is_valid():
            number = serializer.data.get('number')
            holder = serializer.data.get('holder_name')
            date = serializer.data.get('date')
            code = serializer.data.get('code')
            Card.objects.create(profile=profile, holder_name=holder, date=date,number=number,code=code)
            return Response({"CARD ADDED SUCCESFULLY!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)