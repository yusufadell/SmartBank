from django.urls import path
from . import views

urlpatterns = [
    path("", views.test, name="home"),
    path("customers/", views.CustomersListView.as_view(), name="customers_list"),
    path("customers/<int:pk>/",
         views.CustomerDetailView.as_view(), name="customer_detail"),
    path("transfer/customer/", views.money_transfer, name="money_transer"),
    
]
