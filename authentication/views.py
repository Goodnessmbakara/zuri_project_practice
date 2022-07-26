from urllib import response
from django.shortcuts import render
from phonenumbers import is_valid_number
from rest_framework import generics,status
from rest_framework.response import Response
from .models import user
from .import serializers


class HelloAuthView(generics.GenericAPIView):
    def get(self,request):
        return Response(data={'message':'Hello Auth'},status=status.HTTP_200_OK)


class UserCreateView(generics.GenericAPIView):
    serializer_class=serializers.UserCreationSerializer

    def post(self,request):
        data=request.data
        serializer=self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save
            return response(data=serializer.data,status=status.HTTP_201_CREATED)

        return response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
