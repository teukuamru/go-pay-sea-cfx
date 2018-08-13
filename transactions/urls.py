from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import TransactionHistoryListCreateView, \
                   TransactionHistoryDetailsView


urlpatterns = [
    path('', TransactionHistoryListCreateView.as_view(),
         name='transaction_history_list_create'),
    path('<int:pk>/', TransactionHistoryDetailsView.as_view(),
         name='transaction_history_details')
]

urlpatterns = format_suffix_patterns(urlpatterns)
