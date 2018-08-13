from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import Account


class ModelTestCase(TestCase):
    def setUp(self):
        self.user_id = 1
        self.go_pay_balance = 0
        self.account = Account(user_id=self.user_id,
                               go_pay_balance=self.go_pay_balance)

    def test_model_can_create_account(self):
        old_count = Account.objects.count()
        self.account.save()
        new_count = Account.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.account_data = {
            'user_id': 1,
            'go_pay_balance': 0,
        }
        self.response = self.client.post(
            reverse('account_list_create'),
            self.account_data,
            format='json'
        )

    def test_api_can_create_an_account(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_an_account(self):
        account = Account.objects.get()
        response = self.client.get(
            reverse('account_details', kwargs={'pk': account.id}),
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, account)

    # def test_api_can_update_account(self):
    #     account = Account.objects.get()
    #     change_account = {'go_pay_balance': 10000}

    #     res = self.client.put(
    #         reverse('account_details', kwargs={'pk': account.id}),
    #         change_account,
    #         format='json'
    #     )

    #     print('balance', account.go_pay_balance)

    #     self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_bucketlist(self):
        account = Account.objects.get()
        response = self.client.delete(
            reverse('account_details', kwargs={'pk': account.id}),
            format='json', 
            follow=True
        )

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
