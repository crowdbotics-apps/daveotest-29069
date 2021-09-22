from rest_framework import authentication
from driver.models import DriverProfile, DriverOrder
from .serializers import DriverProfileSerializer, DriverOrderSerializer
from rest_framework import viewsets


class DriverOrderViewSet(viewsets.ModelViewSet):
    serializer_class = DriverOrderSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = DriverOrder.objects.all()


class DriverProfileViewSet(viewsets.ModelViewSet):
    serializer_class = DriverProfileSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = DriverProfile.objects.all()
