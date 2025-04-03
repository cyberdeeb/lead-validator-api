from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
import secrets

class APIKey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='api_keys')
    hashed_key = models.CharField(max_length=40, unique=True, editable=False) # API key
    created_at = models.DateTimeField(auto_now_add=True) 
    last_used_at = models.DateTimeField(null=True, blank=True)
    regular_request_count = models.IntegerField(default=0) # Tracking regular API calls
    bulk_request_count = models.IntegerField(default=0) # Tracking bulk API calls

    def save(self, *args, **kwargs):
        """Gernerate a random API Key"""
        if not self.hashed_key:
            key = secrets.token_hex(20)
            self.hashed_key = make_password(key)
        super().save(*args, **kwargs)

    def check_key(self, key):
        """Check if provided key matches hashed key"""
        return check_password(key, self.hashed_key)




