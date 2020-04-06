from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from django_rest_framework.quickstart.serializers import UserSerializer, ManufacturerSerializer, ShoeTypeSerializer, ShoeSerializer, ShoeColorSerializer
from django_rest_framework.quickstart.models import Manufacturer, Shoe, ShoeColor, ShoeType


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class ManufacturerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows manufacturers to be viewed or edited.
    """
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes = [permissions.IsAuthenticated]

class ShoeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows shoes to be viewed or edited.
    """
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer
    permission_classes = [permissions.IsAuthenticated]

class ShoeColorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows shoe colors to be viewed or edited.
    """
    queryset = ShoeColor.objects.all()
    serializer_class = ShoeColorSerializer
    permission_classes = [permissions.IsAuthenticated]

class ShoeTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows shoe types to be viewed or edited.
    """
    queryset = ShoeType.objects.all()
    serializer_class = ShoeTypeSerializer
    permission_classes = [permissions.IsAuthenticated]