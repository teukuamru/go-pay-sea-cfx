from rest_framework import generics, status
from rest_framework.response import Response

from accounts.models import Account
from .serializers import TransactionHistorySerializer, \
                         TransactionHistoryPutSerializer
from .models import TransactionHistory


class TransactionHistoryListCreateView(generics.ListCreateAPIView):
    queryset = TransactionHistory.objects.all()
    serializer_class = TransactionHistorySerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        self.change_account_balance(response.data)
        return response

    def change_account_balance(self, data):
        account = Account.objects.get(user_id=data['user'])

        old_balance = account.go_pay_balance
        new_balance = old_balance + data['changed_balance']
        account.go_pay_balance = new_balance

        account.save()


class TransactionHistoryDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TransactionHistory.objects.all()
    serializer_class = TransactionHistorySerializer

    def get_serializer_class(self):
        serializer_class = self.serializer_class

        if self.request.method == 'PUT':
            serializer_class = TransactionHistoryPutSerializer

        return serializer_class
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.restore_account_balance(instance)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def restore_account_balance(self, instance):
        account = Account.objects.get(user_id=str(instance.user))

        old_balance = account.go_pay_balance
        new_balance = old_balance - instance.changed_balance
        account.go_pay_balance = new_balance

        account.save()
