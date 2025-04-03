from django.contrib import admin
from .models import APIKey
# Register your models here.

@admin.register(APIKey)
class APIKeyAdmin(admin.ModelAdmin):
    list_display = ("user", "created_at", "last_used_at", "regular_request_count", "bulk_request_count")
    readonly_fields = ("hashed_key", "created_at", "last_used_at", "regular_request_count", "bulk_request_count")
    search_fields = ("user__username",)