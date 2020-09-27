from rest_framework import serializers
from career_advice.models import *

class CareerAdviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerAdvice
        fields = '__all__'

    def to_representation(self, instance):
        response = super(CareerAdviceSerializer, self).to_representation(instance)
        if instance.thumbnail_image:
            response['thumbnail_image'] = instance.thumbnail_image.url
        if instance.featured_image:
            response['featured_image'] = instance.featured_image.url
        return response

