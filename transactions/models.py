from django.db import models
from accounts.models import CustomUser


class TransactionHistory(models.Model):
    user = models.ForeignKey(CustomUser, to_field='username',
                             on_delete=models.CASCADE)
    changed_balance = models.IntegerField()
    description = models.TextField()
    finished = models.BooleanField(default=False)

    def __str__(self):
        return "%s %i" % (self.user, self.changed_balance)
