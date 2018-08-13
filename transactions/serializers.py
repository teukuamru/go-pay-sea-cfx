from rest_framework import serializers
from .models import TransactionHistory


class TransactionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionHistory
        fields = ('id', 'user', 'changed_balance',
                  'description', 'finished')
