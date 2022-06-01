from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView

from .forms import MoneyTransferForm
from .models import Customers


class CustomersListView(ListView):
    model = Customers
    template_name = "banks/all_customers.html"
    context_object_name = 'customers'


class CustomerDetailView(DetailView):
    model = Customers
    template_name = 'banks/customer_detail.html'


def money_transfer(request):
    if request.method == "POST":
        form = MoneyTransferForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Money transfered successful!!')
            form.save()

            # Get User Object from TransferForm
            transfer_receiver_form = form.cleaned_data.get("transfer_receiver")
            transfer_sender_form = form.cleaned_data.get("transfer_sender")
            transfer_amount = form.cleaned_data.get("transfer_amount")

            # User Object from database
            transfer_sender = Customers.objects.get(
                user=transfer_sender_form.user)
            transfer_receiver = Customers.objects.get(
                user=transfer_receiver_form.user)

            # Now transfer the money!
            transfer_sender.balance -= transfer_amount
            transfer_receiver.balance += transfer_amount

            # Save the changes before redirecting
            transfer_sender.save()
            transfer_receiver.save()

        return redirect("list-customers")
    else:
        form = MoneyTransferForm()
    return render(request, "banks/money_transfer.html", {"form": form})


def test(request):
    return render(request, "banks/index.html")
