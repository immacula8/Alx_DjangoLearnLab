I fixed my URL setup by moving all account-related paths into accounts/urls.py and only including them in the main social_media_api/urls.py under /api/accounts/.

Now my routes look like this:

/api/accounts/register/

/api/accounts/login/

/api/accounts/profile/

The browser worked fine, but Postman failed because I used {{base_url}} without defining it. To fix this, I either:

Used the full URL directly: http://127.0.0.1:8000/api/accounts/register/, or

Created a Postman environment with base_url = http://127.0.0.1:8000.

After that, all endpoints worked correctly in both browser and Postman.

###Implementing User Follows and Feed Functionality###

I built a custom user system by replacing Django’s default model with one that supports extra fields like date_of_birth and profile_photo, along with email-based authentication. Roles, groups, and permissions were added to control access, while strong security settings ensured safe deployment with HTTPS, CSRF protection, and secure cookies.

On top of authentication, I integrated Django REST Framework to provide APIs with serializers, CRUD endpoints, filtering, and token-based authentication. Finally, social features were introduced: users can follow and unfollow each other, and a feed system was developed to display the latest posts from followed users in order of creation.

###Implementing Notifications and Likes Functionality###

The likes and notifications system allows users to engage with posts and stay updated on activities. Users can like and unlike posts, with each like connected to both the user and the post, while preventing duplicates. Notifications are created whenever someone likes a post, follows another user, or comments on a post, and each notification records the recipient, actor, action, and time. Users can view all their updates through the notifications endpoint, where unread items are shown first. This makes the platform more interactive by keeping users informed and engaged.