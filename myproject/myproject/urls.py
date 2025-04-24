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
from api.forms import CustomUserAuthenticationForm, CustomPasswordResetForm
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import LeadVerificationAPIView, CSVLeadVerificationAPIView, CustomLoginView, signup_view, dashboard_view, home_view, generate_view, regenerate_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name='home'),
    path('verify/', LeadVerificationAPIView.as_view()),
    path('bulk-verify/', CSVLeadVerificationAPIView.as_view()),
    path('signup/', signup_view, name='signup'),
    path('login/', CustomLoginView.as_view(template_name='api/login.html', form_class=CustomUserAuthenticationForm), name='login'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='api/password_reset_form.html', email_template_name='api/password_reset_email.html', form_class=CustomPasswordResetForm), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='api/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='api/password_reset_confirm.html', success_url='reset/done/'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='api/password_reset_complete.html'), name='password_reset_complete'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('generate/', generate_view, name='generate'),
    path('regenerate/', regenerate_view, name='regenerate')
]

urlpatterns = format_suffix_patterns(urlpatterns)
