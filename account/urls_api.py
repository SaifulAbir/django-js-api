from django.urls import path
from account.api import IpnAPI


urlpatterns = [
    path('ipn/', IpnAPI.as_view(), name='ipn-api'),
]