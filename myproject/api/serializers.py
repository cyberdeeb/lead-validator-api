from rest_framework import serializers
from .models import Lead, Email, Phone

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['id', 'email', 'email_status']

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ['id', 'phone', 'phone_status']

class LeadSerializer(serializers.ModelSerializer):
    emails = EmailSerializer(many=True, read_only=True)
    phone_numbers = PhoneSerializer(many=True, read_only=True)


    class Meta:
        model = Lead
        fields = ['id', 'email', 'created_at', 'phone', 'emails', 'phone_numbers']