from rest_framework import serializers
from .models import Settings

class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = ['facebook_url', 'linkedin_url', 'twitter_url', 'appstore_url', 'playstore_url',
                  'logo_url', 'address', 'phone', 'zoom', 'job_min_salary', 'job_max_salary','latitude','longitude',
                  'minimum_profile_completeness','regular_member_apply_limit_per_day','regular_member_apply_limit_per_month',
                  'standard_member_apply_limit_per_day','standard_member_apply_limit_per_month', 'admin_email', 'support_email']

