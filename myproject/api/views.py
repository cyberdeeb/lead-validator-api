import pandas as pd
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LeadVerificationSerializer, CSVUploadSerializer
from .utils import verify_email, verify_phone_number

class LeadVerificationAPIView(APIView):
    def post(self, request, format=None):
        serializer = LeadVerificationSerializer(data=request.data)

        # Ensure that the request is valid
        if serializer.is_valid():

            email = serializer.validated_data.get('email')
            phone_number = serializer.validated_data.get('phone_number')
            # Only verify if email exists
            if email:
                verified_email = verify_email(email)
            else:
                verified_email = None
            # Only verify if phone number exists
            if phone_number:
                verified_phone_number = verify_phone_number(phone_number)
            else:
                verified_phone_number = None
            
            response_data = {
                'email': email,
                'phone_number': phone_number,
                'data': {
                    'email_data': verified_email,
                    'phone_number_data': verified_phone_number
                }
            }

            return Response(response_data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CSVLeadVerificationAPIView(APIView):
    def post(self, request):
        serializer = CSVUploadSerializer(data=request.data)
        # Ensure that the request is valid
        if serializer.is_valid():
            file = serializer.validated_data.get('file')

            # Read CSV file
            try:
                df = pd.read_csv(file)
            except Exception as e:
                return Response({f'Error: Invalid CSV format: {e}'}, status=status.HTTP_400_BAD_REQUEST)
            
            verified_data = []
            
            # Iterating using intertuples
            for row in df.itertuples():
                email = row.email
                phone_number = row.phone_number

                # Only verify if email exists
                if email:
                    verified_email = verify_email(email)
                else:
                    verified_email = None
                # Only verify if phone number exists
                if phone_number:
                    verified_phone_number = verify_phone_number(phone_number)
                else:
                    verified_phone_number = None

                verified_data.append({'email': email,
                                        'phone_number': phone_number,
                                        'data': {
                                            'email_data': verified_email,
                                            'phone_number_data': verified_phone_number
                                            }})
                
            return Response(verified_data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)