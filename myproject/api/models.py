from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Lead(models.Model):
    """Model for leads with multiple emails and phone numbers"""
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class Email(models.Model):
    """Stores multiple emails for a single lead"""
    lead = models.ForeignKey(Lead, related_name='emails', on_delete=models.CASCADE)
    email = models.EmailField()
    email_status = models.CharField(max_length=20, default='pending')

class Phone(models.Model):
    """Stores multiple phone numbers for a single lead"""
    lead = models.ForeignKey(Lead, related_name='phone_numbers', on_delete=models.CASCADE)
    phone_number = PhoneNumberField()
    phone_status = models.CharField(max_length=20, default='pending')