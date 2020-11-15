from django.urls import path, include

from feedback.api import FeedbackCreateAPI

urlpatterns = [
    path('feedback/', FeedbackCreateAPI.as_view()),
]