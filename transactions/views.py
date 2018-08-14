from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response

from accounts.models import Account
from .serializers import TransactionHistorySerializer, \
                         TransactionFinalizeSerializer, \
                         TopUpSerializer
from .models import TransactionHistory


def change_account_balance(data):
    account = Account.objects.get(user_id=data['account'])

    old_balance = account.go_pay_balance
    new_balance = old_balance + data['changed_balance']
    account.go_pay_balance = new_balance

    account.save()


class TransactionHistoryListCreateView(generics.ListCreateAPIView):
    queryset = TransactionHistory.objects.all()
    serializer_class = TransactionHistorySerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        change_account_balance(response.data)
        return response


class TransactionHistoryListByUserView(generics.ListAPIView):
    serializer_class = TransactionHistorySerializer
    lookup_url_kwarg = 'user_id'

    def get_queryset(self):
        user_id = self.kwargs.get(self.lookup_url_kwarg)
        queryset = TransactionHistory.objects.filter(account=user_id)
        return queryset


class TransactionHistoryDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TransactionHistory.objects.all()
    serializer_class = TransactionHistorySerializer

    def get_serializer_class(self):
        serializer_class = self.serializer_class

        if self.request.method == 'PUT':
            serializer_class = TransactionFinalizeSerializer

        return serializer_class

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.refund_account_balance(instance)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def refund_account_balance(self, instance):
        account = Account.objects.get(user_id=str(instance.account))

        old_balance = account.go_pay_balance
        new_balance = old_balance - instance.changed_balance
        account.go_pay_balance = new_balance

        account.save()


class TopUpCreateView(generics.CreateAPIView):
    queryset = TransactionHistory.objects.all()
    serializer_class = TopUpSerializer
    lookup_url_kwarg = 'user_id'

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        change_account_balance(response.data)
        return response

    def perform_create(self, serializer):
        self.change_serializer_data(serializer)
        serializer.save()

    def change_serializer_data(self, serializer):
        user_id = self.kwargs.get(self.lookup_url_kwarg)
        account = get_object_or_404(Account, user_id=user_id)
        serializer.validated_data['account'] = account
        self.process_top_up_transaction(serializer)

    def process_top_up_transaction(self, serializer):
        serializer.validated_data['finished'] = True
