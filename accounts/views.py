from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.response import Response

from .serializers import BalanceSerializer, UserSerializer
from .models import Balance, CustomUser


class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserDetailsView(generics.RetrieveDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'


class BalanceCreateView(generics.CreateAPIView):
    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer


class BalanceDetailsView(generics.RetrieveAPIView):
    serializer_class = BalanceSerializer

    def get_object(self):
        username = self.kwargs['username']

        obj = get_object_or_404(Balance, user__username=username)
        self.check_object_permissions(self.request, obj)

        return obj
