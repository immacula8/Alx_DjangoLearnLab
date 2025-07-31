 Authentication and Permission Setup
This API uses Token-based Authentication provided by Django REST Framework (DRF).

1. Authentication
Token Endpoint:
POST /api/token/
Users send their username and password and receive a token in return.

##Headers for Future Requests:

##Authorization: Token your_token_here
Enabled In settings.py:

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}

2. Permissions
All views are protected by default using:

'DEFAULT_PERMISSION_CLASSES': [
    'rest_framework.permissions.IsAuthenticated',
]
This ensures only authenticated users can access most endpoints.
You can override this in specific views using permission_classes.