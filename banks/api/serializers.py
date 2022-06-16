from rest_framework import serializers
from ..models import Customers, Transfers


class TransfersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfers
        fields = "__all__"


class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = "__all__"
