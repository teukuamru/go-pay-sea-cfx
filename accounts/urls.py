from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import AccountListCreateView, AccountDetailsView


urlpatterns = [
    path('', AccountListCreateView.as_view(),
         name='account_list_create'),
    path('<int:user_id>/', AccountDetailsView.as_view(),
         name='account_details')
]

urlpatterns = format_suffix_patterns(urlpatterns)
