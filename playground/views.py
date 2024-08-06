import json

from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Address
from .serializers import UserSerializer, AddressSerializer


@api_view()
def users(request):
    return Response('ok')


@api_view()
def user_detail(request, pk):
    user = get_object_or_404(User, id=pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view()
def all_address(request):
    queryset = Address.objects.all()
    serializer = AddressSerializer(queryset)
    return Response(serializer.data)


@api_view()
def address_detail(request, pk):
    address = get_object_or_404(Address, id=pk)
    serializer = AddressSerializer(address)
    return Response(serializer.data)
