from django.urls import path
from testimonial.api import testimonial_list

urlpatterns = [
    path('testimonial_show/',testimonial_list) # Public API
]