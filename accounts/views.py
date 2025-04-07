from django.shortcuts import render
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from accounts.serializers import UserSerializer
from rest_framework import status


class RegisterAPIView(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        ser_data = UserSerializer(data=request.data)
        if ser_data.is_valid():
            user = ser_data.save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)