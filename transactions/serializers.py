from rest_framework import serializers

from .models import TransactionHistory


class TransactionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionHistory
        fields = ('changed_balance', 'description')


class TransactionFinalizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionHistory
        fields = '__all__'
        read_only_fields = ('user_balance', 'changed_balance', 'description')


class TopUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionHistory
        fields = '__all__'
        read_only_fields = ('user_balance', 'finished',)
