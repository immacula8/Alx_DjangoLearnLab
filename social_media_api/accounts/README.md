I fixed my URL setup by moving all account-related paths into accounts/urls.py and only including them in the main social_media_api/urls.py under /api/accounts/.

Now my routes look like this:

/api/accounts/register/

/api/accounts/login/

/api/accounts/profile/

The browser worked fine, but Postman failed because I used {{base_url}} without defining it. To fix this, I either:

Used the full URL directly: http://127.0.0.1:8000/api/accounts/register/, or

Created a Postman environment with base_url = http://127.0.0.1:8000.

After that, all endpoints worked correctly in both browser and Postman.