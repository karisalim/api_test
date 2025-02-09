from rest_framework import serializers
from django.contrib.auth.models import User


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
        extra_kwargs = {
            'first_name': {'required': True, 'allow_blank': False},
            'last_name': {'required': True, 'allow_blank': False},
            'email': {'required': True, 'allow_blank': False},
            'password': {'required': True, 'allow_blank': False, 'min_length': 8},
        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']








# from django.contrib.auth.models import User
# from rest_framework import serializers
#
# class SignUpSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email', 'password']
#         extra_kwargs = {
#             'password': {
#                 'write_only': True,
#                 'required': True,
#                 'min_length': 8
#             },
#             'email': {'required': True}
#         }
#
#     def create(self, validated_data):
#         password = validated_data.pop('password', None)
#         user = User(**validated_data)
#         if password:
#             user.password = make_password(password)
#         user.save()
#         return user
#
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email', 'username']
