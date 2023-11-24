from rest_framework import viewsets
from news.models import User
from news_rest.serializers.user_serializer import UserSerializer


class User(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
