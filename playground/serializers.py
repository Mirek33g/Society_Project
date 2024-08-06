from rest_framework import serializers
from .models import Address


class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    phone = serializers.CharField(max_length=255)
    user_address = serializers.PrimaryKeyRelatedField(
        queryset=Address.objects.all()
    )


class AddressSerializer(serializers.Serializer):
    address = serializers.CharField(max_length=255)
