from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import TransactionHistoryListCreateView, \
                   TransactionHistoryDetailsView, \
                   TransactionHistoryListByUserView, \
                   TopUpCreateView


urlpatterns = [
    path('', TransactionHistoryListCreateView.as_view(),
         name='transaction_history_list_create'),
    path('<int:pk>/', TransactionHistoryDetailsView.as_view(),
         name='transaction_history_details'),
    path('all/<str:user_id>/',
         TransactionHistoryListByUserView.as_view(),
         name='transaction_history_list_by_user'),
    path('top-up/<str:user_id>', TopUpCreateView.as_view(),
         name='top_up_create'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
