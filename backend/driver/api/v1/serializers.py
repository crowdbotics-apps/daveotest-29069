from rest_framework import serializers
from driver.models import DriverProfile, DriverOrder


class DriverOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverOrder
        fields = "__all__"


class DriverProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverProfile
        fields = "__all__"
