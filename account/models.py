from django.db import models
from django.db.models.signals import pre_save

from p7.models import P7Model, populate_time_info
from resources import strings_account


class TransactionHistory(P7Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    bank_tran_id = models.CharField(max_length=80)
    base_fair = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    card_brand = models.CharField(max_length=30)
    card_issuer = models.CharField(max_length=50)
    card_issuer_country = models.CharField(max_length=50)
    card_issuer_country_code = models.CharField(max_length=2)
    card_no = models.CharField(max_length=80, null=True)
    card_sub_brand = models.CharField(max_length=30, null=True)
    card_type = models.CharField(max_length=50, null=True)
    currency = models.CharField(max_length=3)
    currency_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    currency_rate = models.DecimalField(max_digits=10, decimal_places=4)
    currency_type = models.CharField(max_length=3)
    error = models.CharField(max_length=255, null=True, blank=True)
    risk_level = models.PositiveIntegerField(null=True, blank=True)
    risk_title = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=20)
    store_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    store_id = models.CharField(max_length=50)
    tran_date = models.DateTimeField(blank=False, null=False)
    tran_id = models.CharField(max_length=30)
    val_id = models.CharField(max_length=50)
    value_a = models.CharField(max_length=255, null=True, blank=True)
    value_b = models.CharField(max_length=255, null=True, blank=True)
    value_c = models.CharField(max_length=255, null=True, blank=True)
    value_d = models.CharField(max_length=255, null=True, blank=True)
    verify_sign = models.CharField(max_length=255)
    verify_sign_sha2 = models.CharField(max_length=255)
    emi_instalment = models.PositiveIntegerField(null=True, blank=True)
    emi_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount_percentage = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount_remarks = models.CharField(max_length=255, null=True, blank=True)
    gateway = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        db_table = 'transaction_histories'
        verbose_name = strings_account.SSLCOMMERZ_TRANSACTION
        verbose_name_plural = strings_account.SSLCOMMERZ_TRANSACTION_NAME_PLURAL

    def __str__(self):
        return self.tran_id


pre_save.connect(populate_time_info, sender=TransactionHistory)
