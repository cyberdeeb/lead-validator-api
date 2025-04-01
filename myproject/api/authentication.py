from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.utils.timezone import now
from .models import APIKey

class APIKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        api_key = request.headers.get('X-API-Key') # Pull API key from headers

        if not api_key:
            return None
        # Verify the API Key
        try:
            key = APIKey.objects.get(key=api_key)
        except APIKey.DoesNotExist:
            raise AuthenticationFailed('Invalid API Key')
        
        # Determine verification request type to track usage
        is_bulk = request.path.startswith('/bulk-verify/')

        # Update last used timestamp
        key.last_used_at = now()

        # Increment count based on request type
        if is_bulk:
            key.bulk_request_count += 1
        else:
            key.regular_request_count += 1

        key.save(
            update_fields=['last_used_at', 'bulk_request_count', 'regular_request_count']
        )

        
        return (key, None)