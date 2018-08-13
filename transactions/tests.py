from django.test import TestCase

from .models import TransactionHistory
from accounts.models import Account


class ModelTestCase(TestCase):
    def setUp(self):
        self.user = Account.objects.create(user=1,
                                           go_pay_balance=0)
        self.changed_balance = -10000
        self.description = 'jalan jalan'
        self.finished = False

        self.transaction_history = \
            TransactionHistory(user=self.user,
                               changed_balance=self.changed_balance,
                               description=self.description,
                               finished=self.finished)

    def test_model_can_create_transaction_history(self):
        old_count = TransactionHistory.objects.count()
        self.transaction_history.save()
        new_count = TransactionHistory.objects.count()
        self.assertNotEqual(old_count, new_count)
