from rest_framework import serializers
from .models import TransactionHistory


class TransactionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionHistory
        fields = '__all__'


class TransactionHistoryPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionHistory
        fields = '__all__'
        read_only_fields = ('user', 'changed_balance', 'description')
