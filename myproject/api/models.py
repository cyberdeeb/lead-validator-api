from django.db import models
import secrets

class APIKEY(models.Model):
    name = models.CharField(max_length=255)
    key = models.CharField(max_length=40, unique=True, editable=False) # API key
    created_at = models.DateTimeField(auto_now_add=True) 
    last_used_at = models.DateTimeField(null=True, blank=True)
    regular_request_count = models.IntegerField(default=0) # Tracking regular API calls
    bulk_request_count = models.IntegerField(default=0) # Tracking bulk API calls

    def save(self, *args, **kwargs):
        """Gernerate a random API Key"""
        if not self.key:
            self.key = secrets.token_hex(20)
        super().save(*args, **kwargs)





