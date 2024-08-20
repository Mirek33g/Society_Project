from rest_framework import serializers
from .models import Address, Post, User


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'address', 'user']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'post_type', 'placed_at', 'user']


class UserSerializer(serializers.ModelSerializer):
    user_address = AddressSerializer(read_only=True)
    user_post = PostSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone', 'user_address', 'user_post']
