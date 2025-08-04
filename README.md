# Lead Verification API

A professional Django REST API for validating email addresses and phone numbers with comprehensive authentication, rate limiting, and production deployment capabilities.

🌐 **Live Demo:** [https://lead-validator-api-production.up.railway.app/](https://lead-validator-api-production.up.railway.app/)

## Overview

The Lead Verification API is a production-ready Django REST API that validates email addresses and phone numbers using third-party services like Hunter.io and Twilio. Built as a portfolio project, it demonstrates professional API development practices including authentication, rate limiting, data processing, and production deployment.

## ✨ Features

- **Email Verification** - Validate email addresses using Hunter.io (validity, disposability, risk scoring)
- **Phone Number Verification** - Verify phone numbers using Twilio (validity, line type, carrier info)
- **Bulk Processing** - CSV upload support for batch lead verification
- **API Key Authentication** - Secure authentication system with usage tracking
- **Rate Limiting** - Built-in protection against abuse (5 requests/month for demo)
- **Professional UI** - Clean, responsive web interface with Bulma CSS
- **Comprehensive Documentation** - Complete API documentation with code examples
- **Production Ready** - Deployed on Railway with PostgreSQL database

## 🚀 Quick Start

1. **Visit the Live Demo:** [https://lead-validator-api-production.up.railway.app/](https://lead-validator-api-production.up.railway.app/)
2. **Sign Up** for an account
3. **Generate** your API key from the dashboard
4. **Start verifying** leads using the API endpoints

## 📡 API Endpoints

### Authentication

All requests require an API key in the header:

```
X-API-Key: your-api-key-here
```

### Single Lead Verification

```bash
POST https://lead-validator-api-production.up.railway.app/verify/
Content-Type: application/json
X-API-Key: your-api-key-here

{
    "email": "test@example.com",
    "phone_number": "+1234567890"
}
```

### Bulk CSV Verification

```bash
POST https://lead-validator-api-production.up.railway.app/bulk-verify/
Content-Type: multipart/form-data
X-API-Key: your-api-key-here

file: leads.csv
```

## 💻 Code Examples

### Python

```python
import requests

url = "https://lead-validator-api-production.up.railway.app/verify/"
headers = {
    "Content-Type": "application/json",
    "X-API-Key": "your-api-key-here"
}
data = {
    "email": "test@example.com",
    "phone_number": "+1234567890"
}

response = requests.post(url, json=data, headers=headers)
result = response.json()
print(result)
```

### JavaScript

```javascript
const response = await fetch(
  'https://lead-validator-api-production.up.railway.app/verify/',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-API-Key': 'your-api-key-here',
    },
    body: JSON.stringify({
      email: 'test@example.com',
      phone_number: '+1234567890',
    }),
  }
);

const result = await response.json();
console.log(result);
```

### cURL

```bash
curl -X POST "https://lead-validator-api-production.up.railway.app/verify/" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: your-api-key-here" \
  -d '{
    "email": "test@example.com",
    "phone_number": "+1234567890"
  }'
```

## 🛠️ Tech Stack

### Backend

- **Django 5.2.4** - Web framework
- **Django REST Framework 3.16.0** - API framework
- **Python 3.13.5** - Programming language

### Database

- **PostgreSQL** - Production database (Railway)
- **SQLite** - Development database

### Third-Party Services

- **Hunter.io** - Email verification service
- **Twilio** - Phone number verification service

### Frontend & Styling

- **Bulma CSS** - Modern CSS framework
- **Crispy Forms** - Enhanced form rendering
- **Font Awesome** - Icons and UI elements

### Authentication & Security

- **Custom API Key Authentication** - Secure API access
- **Rate Limiting** - Request throttling
- **CSRF Protection** - Security middleware
- **SSL/HTTPS** - Secure connections in production

### Deployment & Infrastructure

- **Railway** - Cloud hosting platform
- **WhiteNoise** - Static file serving
- **Gunicorn** - WSGI HTTP server
- **Environment Variables** - Configuration management

## 📊 Response Format

### Email Verification Response

```json
{
  "email": "test@example.com",
  "phone_number": "+1234567890",
  "data": {
    "email_data": {
      "valid": true,
      "score": 85,
      "disposable": false
    },
    "phone_number_data": {
      "valid": true,
      "line_type": "mobile",
      "validation_errors": []
    }
  }
}
```

### Error Responses

| Status Code | Description         | Example Response                                         |
| ----------- | ------------------- | -------------------------------------------------------- |
| 401         | Invalid API key     | `{"detail": "Invalid API Key"}`                          |
| 400         | Bad request         | `{"error": "Either email or phone number are required"}` |
| 429         | Rate limit exceeded | `{"detail": "Request was throttled"}`                    |
| 500         | Server error        | `{"error": "Internal server error"}`                     |

## 🏗️ Local Development

### Prerequisites

- Python 3.13+
- Virtual environment
- Git

### Setup

```bash
# Clone the repository
git clone https://github.com/cyberdeeb/lead-validator-api.git
cd lead-validator-api

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys

# Run migrations
cd myproject
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start development server
python manage.py runserver
```

### Environment Variables

```bash
# Third-party API keys
HUNTER_API_KEY=your_hunter_api_key
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_token

# Email configuration (optional for development)
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password

# Production settings (Railway deployment)
DATABASE_URL=postgresql://...
RAILWAY_ENVIRONMENT=production
```

## 🌟 Key Features Demonstrated

- **Professional API Design** - RESTful endpoints with proper HTTP methods
- **Authentication & Authorization** - Custom API key authentication system
- **Data Validation** - Comprehensive input validation and error handling
- **Third-party Integrations** - Hunter.io and Twilio API integrations
- **Bulk Data Processing** - CSV upload and processing with pandas
- **Rate Limiting** - Request throttling for API protection
- **Production Deployment** - Full Railway deployment with PostgreSQL
- **Documentation** - Complete API documentation with examples
- **User Interface** - Professional web interface for API management

## 📝 Portfolio Context

This project demonstrates:

- **Backend Development** - Django and DRF expertise
- **API Development** - RESTful design and implementation
- **Database Design** - Model relationships and migrations
- **Authentication Systems** - Custom authentication implementation
- **Third-party Integrations** - External API consumption
- **Production Deployment** - Cloud hosting and database management
- **Documentation** - Technical writing and API documentation
- **UI/UX Design** - Responsive web interface design

## 👤 Developer

**Abraham Deeb**

- Portfolio Project showcasing Django and API development skills
- Available for backend development, API integrations, and Django applications
- Contact via the [Contact Us](https://lead-validator-api-production.up.railway.app/contact/) page

## 📄 License

This project is a portfolio demonstration. For production use or collaboration inquiries, please contact the developer.

---

_Built with Django REST Framework • Deployed on Railway • Created by Abraham Deeb_
