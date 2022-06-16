from rest_framework import generics

from ..models import Customers, Transfers
from .serializers import CustomersSerializer, TransfersSerializer


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
