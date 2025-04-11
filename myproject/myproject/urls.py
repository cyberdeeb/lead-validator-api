"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from api.forms import CustomUserAuthenticationForm
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import LeadVerificationAPIView, CSVLeadVerificationAPIView, CustomLoginView, signup_view, dashboard_view, home_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name='home'),
    path('verify/', LeadVerificationAPIView.as_view()),
    path('bulk-verify/', CSVLeadVerificationAPIView.as_view()),
    path('signup/', signup_view, name='signup'),
    path('login/', CustomLoginView.as_view(template_name='api/login.html', form_class=CustomUserAuthenticationForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
