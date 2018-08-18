from django.db import models
from accounts.models import Balance


class TransactionHistory(models.Model):
    user_balance = models.ForeignKey(Balance, to_field='user',
                                     on_delete=models.CASCADE)
    changed_balance = models.IntegerField()
    description = models.TextField()
    finished = models.BooleanField(default=False)

    def __str__(self):
        return "%s %i" % (self.user_balance, self.changed_balance)
