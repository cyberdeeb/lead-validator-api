from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField

class LeadVerificationSerializer(serializers.Serializer):

    email = serializers.EmailField(required=False)
    phone_number = PhoneNumberField(required=False)

    def validate(self, data):
        if not data.get('email') or not data.get('phone_number'):
            raise serializers.ValidationError('Either email or phone number are required')
        return data