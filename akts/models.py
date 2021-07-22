from django.db import models
from account.models import User
from institution.models import Address


class Akt(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipients')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='senders')
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='adres')
    fio = models.CharField(max_length=50, blank=True, null=True)
    position = models.CharField(max_length=50, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=False)
    inventory = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'Akt --> {self.id}'

