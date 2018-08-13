from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('user_id', 'go_pay_balance')
        read_only_fields = ('go_pay_balance', )
