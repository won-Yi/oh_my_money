from django.db import models
from user.models import User

class Ledger(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    money = models.CharField(max_length=256)
    memo = models.CharField(max_length=256, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table ='ledger'
