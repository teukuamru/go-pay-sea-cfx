from django.db import models


class Account(models.Model):
    user_id = models.IntegerField(primary_key=True)
    go_pay_balance = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user_id)

    def __unicode__(self):
        return str(self.user_id)
