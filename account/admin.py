from django.contrib import admin

# Register your models here.
from account.models import TransactionHistory

admin.site.register(TransactionHistory)