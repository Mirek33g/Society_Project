from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer


@api_view()
def users(request):
    return Response('ok')


@api_view()
def user_detail(request, tk):
    user = User.objects.get(pk=tk)
    serializer = UserSerializer(user)
    return Response(serializer.data)
