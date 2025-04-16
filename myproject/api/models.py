from datetime import timedelta
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
import secrets

class APIKey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='api_keys')
    hashed_key = models.CharField(max_length=40, unique=True, editable=False) # API key
    created_at = models.DateTimeField(auto_now_add=True) 
    last_used_at = models.DateTimeField(null=True, blank=True)
    last_regenerated = models.DateTimeField(null=True, blank=True)
    regular_request_count = models.IntegerField(default=0) # Tracking regular API calls
    bulk_request_count = models.IntegerField(default=0) # Tracking bulk API calls
    is_inactive = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        """Gernerate a random API Key"""
        #Generate if there is no hashed key yet
        if not self.hashed_key:
            new_key = secrets.token_hex(20)
            self.hashed_key = make_password(new_key)
            self._plain_key = new_key # Temporarly store plain key to share with user once
        super().save(*args, **kwargs)

    def check_key(self, key):
        """Check if provided key matches hashed key"""
        return check_password(key, self.hashed_key)
    
    def regenerate_key(self):
        # Check if this is the first key ever (never been regenerated)
        if self.last_regenerated == None:
            last_regenerated_time = self.created_at
        else:
            last_regenerated_time = self.last_regenerated

        # Check if API key has been regenerated within the past month
        if last_regenerated_time + timedelta(days=30) > timezone.now():
            raise ValueError('You can only regenerate your API Key once per month.')
        
        # Current key is marked inactive
        self.is_inactive = True
        self.save()

        # Generate a new API key instance
        new_key = secrets.token_hex(20)
        new_api_key = APIKey.objects.create(
            user=self.user,
            hashed_key=make_password(new_key),
            last_regenerated = timezone.now()
        )
        
        # Return new key to show user once in plain text
        return new_key

    
    @property
    def prefix(self):
        return self.hashed_key[:8]




