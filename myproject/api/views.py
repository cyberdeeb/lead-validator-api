import pandas as pd
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .authentication import APIKeyAuthentication
from .models import APIKey
from .serializers import LeadVerificationSerializer, CSVUploadSerializer
from .utils import verify_email, verify_phone_number

# API Views
class LeadVerificationAPIView(APIView):

    # Require API key
    authentication_classes = [APIKeyAuthentication]
    # Only accessed by authenticated users
    permission_classes = [IsAuthenticated]

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

    # Require API key
    authentication_classes = [APIKeyAuthentication]
    # Only accessed by authenticated users
    permission_classes = [IsAuthenticated]

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
    
# Web views
def home_view(request):
    return render(request, 'api/home.html')


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
            form = CustomUserCreationForm()

    return render(request, 'api/signup.html', {'form':form}) 

class CustomLoginView(LoginView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)
    
@login_required
def dashboard_view(request):
    api_keys = APIKey.objects.filter(user=request.user)
    return render(request, 'api/dashboard.html', {'api_keys': api_keys})

@login_required
# Used for first time API Key generation
def generate_view(request):
    if request.method == 'POST':
        try:
            # Verify user does not already have an active API key
            if APIKey.objects.filter(user=request.user, is_inactive=False).exists():
                messages.error(request, 'You already have an active API Key.')
            else:
                # Create and save the new key
                api_key = APIKey(user=request.user)
                api_key.save()

                # Access the temporary plain key
                if hasattr(api_key, '_plain_key'):
                    messages.success(request, f'Your API key: {api_key._plain_key}')
                else:
                    messages.error(request, 'Something went wrong during key generation')

        except ValueError as e:
            messages.error(request, f'{str(e)}')
        return redirect('dashboard')
    
    return redirect('dashboard')

@login_required
# Used when regenerate button clicked by user
def regenerate_view(request):
    if request.method == 'POST':
        try:
            api_key = APIKey.objects.filter(user=request.user, is_inactive=False).first()
            new_key = api_key.regenerate_key()
            messages.success(request, f'Your API key: {new_key}')
            messages.warning(request, 'Please save your API Key in a secure location. This will only be shared once and you can only regenerate a key every 30 days.')
        except ValueError as e:
            messages.error(request, f'{str(e)}')
        return redirect('dashboard')
    return redirect('dashboard')
    

