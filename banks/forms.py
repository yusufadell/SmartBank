from django import forms
from .models import Transfers


class MoneyTransferForm (forms.ModelForm):
    class Meta:
        model = Transfers
        fields = [
            "transfer_sender",
            "transfer_receiver",
            "transfer_amount"
        ]
