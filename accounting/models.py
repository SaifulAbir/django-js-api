from django.db import models
from django.db.models.signals import pre_save

from p7.models import P7Model, populate_time_info
from resources import strings_job

class TransactionHistory(P7Model):
    tran_date = models.DateTimeField(blank=False,null=False)
    tran_id = models.CharField(max_length=30)
    val_id = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    store_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    card_type = models.CharField(max_length=50)
    card_no = models.CharField(max_length=80)
    currency = models.CharField(max_length=3)
    bank_tran_id = models.CharField(max_length=80)
    card_issuer = models.CharField(max_length=50)
    card_brand = models.CharField(max_length=30)
    card_issuer_country = models.CharField(max_length=50)
    card_issuer_country_code = models.CharField(max_length=2)
    currency_type = models.CharField(max_length=3)
    currency_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    emi_instalment = models.PositiveIntegerField(max_length=2, null=True, blank=True)
    emi_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount_percentage = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount_remarks = models.CharField(max_length=255, null=True, blank=True)
    value_a = models.CharField(max_length=255, null=True, blank=True)
    value_b = models.CharField(max_length=255, null=True, blank=True)
    value_c = models.CharField(max_length=255, null=True, blank=True)
    value_d = models.CharField(max_length=255, null=True, blank=True)
    risk_level = models.PositiveIntegerField(max_length=1)
    risk_title = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    gateway = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        verbose_name = strings_job.SSLCOMMERZ_TRANSACTION
        verbose_name_plural = strings_job.SSLCOMMERZ_TRANSACTION_NAME_PLURAL

    def __str__(self):
        return self.tran_id

pre_save.connect(populate_time_info, sender=TransactionHistory)
