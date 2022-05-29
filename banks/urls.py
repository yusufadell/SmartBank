# TODO: update url patterns
from django.urls import path
from . import views

urlpatterns = [
    path("customers/", views.CustomersListView.as_view(), name="list-customers"),
    path("customers/<int:pk>/",
         views.CustomerDetailView.as_view(), name="customer_detail"),
    path("customer/transfer/", views.money_transfer, name="money-trans"),
    path("", views.test, name="home")
]
