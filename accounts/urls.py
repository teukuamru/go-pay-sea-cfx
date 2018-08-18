from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import BalanceCreateView, BalanceDetailsView, \
                   UserListView, UserDetailsView


urlpatterns = [
    path('', UserListView.as_view(),
         name='account_list_create'),
    path('<str:username>/', UserDetailsView.as_view(),
         name='account_details'),

    path('<str:username>/balance/create/', BalanceCreateView.as_view(),
         name='balance_create'),
    path('<str:username>/balance/', BalanceDetailsView.as_view(),
         name='balance_details'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
