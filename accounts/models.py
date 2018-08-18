from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    name = models.CharField(max_length=500)
    driver = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Balance(models.Model):
    user = models.OneToOneField(CustomUser, to_field='username',
                                on_delete=models.CASCADE)
    go_pay_balance = models.IntegerField(default=0)

    def __str__(self):
        return '%s %i' % (self.user, self.go_pay_balance)
