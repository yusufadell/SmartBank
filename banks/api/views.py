from rest_framework import generics
from ..models import Transfers, Customers
from .serializers import TransfersSerializer, CustomersSerializer


class TransfersListView(generics.ListCreateAPIView):
    queryset = Transfers.objects.all()
    serializer_class = TransfersSerializer


class TransfersDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transfers.objects.all()
    serializer_class = TransfersSerializer


class CustomersListView(generics.ListCreateAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer


class CustomersDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer
