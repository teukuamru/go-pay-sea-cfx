from django.db import models
from accounts.models import Account


class TransactionHistory(models.Model):
    account = models.ForeignKey(Account, to_field='user_id',
                             on_delete=models.CASCADE)
    changed_balance = models.IntegerField()
    description = models.TextField()
    finished = models.BooleanField(default=False)

    def __str__(self):
        return "%s %i" % (self.user, self.changed_balance)
