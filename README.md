# Lead Verification API

## Overview

The Lead Verification API is a Django REST API that validates email addresses and phone numbers using third-party services like Hunter.io and Twilio. It is designed to help businesses verify leads, ensuring that contact information is accurate before being used in marketing or CRM systems.

## Features

* Validate email addresses using Hunter.io (checks for validity, disposability, and risk level)
* Verify phone numbers using Twilio (checks if the number is valid, mobile, landline, or VoIP)
* Support for bulk lead verification via CSV upload
* API authentication using JWT (JSON Web Tokens)
* Rate limiting to prevent abuse
* Error handling and logging
* Scalable and deployable using Docker, AWS, or Heroku

## Tech Stack

* **Backend:** Django, Django REST Framework (DRF)
* **Database:** PostgreSQL
* **Third-Party Services:** Hunter.io (for email verification), Twilio (for phone verification)
* **Authentication:** JWT (JSON Web Tokens)
* **Deployment:** Docker, AWS, or Heroku
