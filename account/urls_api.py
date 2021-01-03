from django.urls import path
from account.api import IpnAPI


urlpatterns = [
    path('api/ipn/', IpnAPI.as_view(), name='ipn-api'),
]