from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Address, Post
from .serializers import UserSerializer, AddressSerializer, PostSerializer


@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


@api_view(['GET'])
def user_detail(request, pk):
    user = get_object_or_404(User, id=pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(['GET'])
def address_list(request):
    queryset = Address.objects.all()
    serializer = AddressSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def address_detail(request, pk):
    address = get_object_or_404(Address, id=pk)
    serializer = AddressSerializer(address)
    return Response(serializer.data)


@api_view(['GET'])
def post_list(request):
    queryset = Post.objects.all()
    serializer = PostSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def post_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    serializer = PostSerializer(post)
    return Response(serializer.data)
