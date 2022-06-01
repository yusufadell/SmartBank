# TODO: create model related more related to banks

from django.db import models
from django.contrib.auth.models import User


class Customers(models.Model):
    """Customers Table representation with basic info 

    :param models: Django ORM Model
    :type models: DB Fields
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=50, default=None)
    email = models.EmailField()
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    account_number = models.AutoField(primary_key=True)

    def __str__(self):
        return f"{self.user_name} (${self.balance}) "


class Transfers(models.Model):
    """
    Transfers record all transfers happened

    :param models: record all transfers happened
    :type models: Cash
    """
    transfer_sender = models.ForeignKey(
        Customers, on_delete=models.CASCADE, related_name="transfer_sender")
    transfer_receiver = models.ForeignKey(
        Customers, on_delete=models.CASCADE, related_name="transfer_receiver")
    transfer_amount = models.DecimalField(max_digits=10, decimal_places=2)
    transfer_created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        ordering = ('-transfer_created',)

    def __str__(self) -> str:
        return f"{self.transfer_created.strftime('%X %x %Z')} - {self.transfer_sender} sends ${self.transfer_amount} to {self.transfer_receiver}"
