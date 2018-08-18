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

    def get_queryset(self):
        username = self.kwargs['username']
        print(username)

        return Balance.objects.filter(user__username=username)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        serializer.data.user = CustomUser.objects.get(id=1).username

        return Response(serializer.data)
