from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response

from accounts.models import Balance, CustomUser
from .serializers import TransactionHistorySerializer, \
                         TransactionFinalizeSerializer, \
                         TopUpSerializer, TransactionHistoryDetailsSerializer
from .models import TransactionHistory


def change_account_balance(data):
    balance = Balance.objects.get(user=data['user'])

    old_balance = balance.go_pay_balance
    new_balance = old_balance + data['changed_balance']
    balance.go_pay_balance = new_balance

    balance.save()


class TransactionHistoryListCreateView(generics.ListCreateAPIView):
    queryset = TransactionHistory.objects.all()
    serializer_class = TransactionHistorySerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        change_account_balance(response.data)
        return response


class TransactionHistoryListByUserView(generics.ListAPIView):
    serializer_class = TransactionHistorySerializer
    lookup_url_kwarg = 'username'

    def get_queryset(self):
        username = self.kwargs.get(self.lookup_url_kwarg)
        queryset = TransactionHistory.objects.filter(user__username=username)
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
        user_balance = Balance.objects.get(user=instance.user)

        old_balance = user_balance.go_pay_balance
        new_balance = old_balance - instance.changed_balance
        user_balance.go_pay_balance = new_balance

        user_balance.save()


class TopUpCreateView(generics.CreateAPIView):
    queryset = TransactionHistory.objects.all()
    serializer_class = TopUpSerializer
    lookup_url_kwarg = 'username'

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        change_account_balance(response.data)

        # user = response.data['user']
        # response.data['user'] = user.username

        return response

    def perform_create(self, serializer):
        self.change_serializer_data(serializer)
        serializer.save()

    def change_serializer_data(self, serializer):
        username = self.kwargs.get(self.lookup_url_kwarg)
        user = get_object_or_404(CustomUser, username=username)

        serializer.validated_data['user'] = user

        self.process_top_up_transaction(serializer)

    def process_top_up_transaction(self, serializer):
        serializer.validated_data['finished'] = True
