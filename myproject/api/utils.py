import os
import json
import requests
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

def verify_email(email):
    """Verifies an email address using the Hunter.io Email Verifier API."""
    hunter_key = os.getenv('HUNTER_API_KEY')
    url = f"https://api.hunter.io/v2/email-verifier?email={email}&api_key={hunter_key}"
    
    try:
        response = requests.get(url)
        # Raise HTTPError for bad responses
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return {'error':str(e)}
    # Parse JSON response
    data = response.json()
    # Return the status of the email
    return data['data']['status']

def verify_phone_number(phone_number):
    """Verifies phone numbers using the Twilio Lookup API"""
    account_sid = os.environ["TWILIO_ACCOUNT_SID"]
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    client = Client(account_sid, auth_token)

    data = client.lookups.v2.phone_numbers(phone_number).fetch()
    # Return the status of phone number
    return data.valid
