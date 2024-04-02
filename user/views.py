from rest_framework.viewsets import ModelViewSet
from . import models, serializers
from rest_framework.permissions import IsAuthenticated


class UserViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
