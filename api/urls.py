# api/urls.py
from django.urls import include, path
from .views import CustomObtainAuthToken

urlpatterns = [
    path('accounts/', include('accounts.urls')),

    path('rest-auth/login/', CustomObtainAuthToken.as_view()),
    path('rest-auth/', include('rest_auth.urls')),

    path('rest-auth/registration/', include('rest_auth.registration.urls')),

    path('transactions/', include('transactions.urls')),
]