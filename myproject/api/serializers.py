from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField

class LeadVerificationSerializer(serializers.Serializer):

    email = serializers.EmailField(required=False)
    phone_number = serializers.CharField(required=False)

    def validate(self, data):
        if not data.get('email') and not data.get('phone_number'):
            raise serializers.ValidationError('Either email or phone number are required')
        return data