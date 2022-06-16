from django.urls import path

from .views import CustomersDetailView
from .views import CustomersListView
from .views import TransfersDetailView
from .views import TransfersListView

app_name = "banks"

urlpatterns = [
    path("transfers/", TransfersListView.as_view(), name="transfers-list"),
    path("transfers/<int:pk>/",
         TransfersDetailView.as_view(),
         name="transfers-detail"),
    path("customers/", CustomersListView.as_view(), name="customers"),
    path("customers/<int:pk>/",
         CustomersDetailView.as_view(),
         name="customers-detail"),
]
