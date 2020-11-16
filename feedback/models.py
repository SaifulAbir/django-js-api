from django.db import models

# Create your models here.
from p7.models import P7Model
from p7.validators import check_valid_phone_number
from resources import strings_feedback


class Feedback(P7Model):
    name = models.CharField(max_length=255,)
    email = models.CharField(max_length=255,)
    phone = models.CharField(max_length=255, validators=[check_valid_phone_number], blank=True, null=True)
    feedback = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = strings_feedback.FEEDBACK_VERBOSE_NAME
        verbose_name_plural = strings_feedback.FEEDBACK_VERBOSE_NAME_PLURAL
        db_table = 'feedbacks'
        ordering = ['-created_at']