from enum import unique
from django.db import models
from django.forms import PasswordInput
import phonenumber_field
from.models import user
from rest_framework import serializers


class UserCreationSerializer(serializers.ModelSerializer):
    username=models.CharField(max_length=25,unique=True)
    email=models.EmailField(max_length=80,unique=True)
    phone_number=phonenumber_field(null=False,unique=True)
    password=serializers.CharField(min_length=8)


    def Meta():
        model=user
        fields=['username','email','phone_number','password']


    def validate(self, attrs):
        username_exists = user.objects.filter(username=attrs['username']).exists
        if username_exists:
            raise serializers.ValidationError(detail=f'user with username exists')

        email_exists = user.objects.filter(email=attrs['email']).exists
        if email_exists:
            raise serializers.ValidationError(detail=f'user with email exists')

        phonenumber_exists = user.objects.filter(phonenumber=attrs['phone_number']).exists
        if phonenumber_exists:
            raise serializers.ValidationError(detail=f'user with phonenumber exists')


        return super().validate(attrs)

        