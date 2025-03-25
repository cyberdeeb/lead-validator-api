from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from serializers import LeadVerificationSerializer
from utils import verify_email, verify_phone_number

class LeadVerificationAPIview(APIView):
    def post(self, request, format=None):
        serialzer = LeadVerificationSerializer(data=request.data)

        # Ensure that the 
        if serialzer.is_valid():

            email = serialzer.validated_data.get('email')
            phone_number = serialzer.validated_data.get('phone_number')

            if email:
                verified_email = verify_email(email)

            if phone_number:
                verified_phone_number = verify_phone_number(phone_number)
            
            response_data = {
                'email': email,
                'phone_number': phone_number,
                'data': {
                    'email_data': verified_email,
                    'phone_number_data': verified_phone_number
                }
            }

            return Response(response_data, status=status.HTTP_200_OK)
        
        return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)

