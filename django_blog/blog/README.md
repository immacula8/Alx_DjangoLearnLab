Authentication Documentation
This Django project uses the built-in authentication system to handle user login, logout, registration, and profile access.

Users can register for a new account on the /register/ page by providing their username, email, and password. After registering, they can log in at /login/ with their username and password.

Once logged in, users can access their profile page at /profile/. If a user tries to visit the profile without logging in, Django will redirect them to the login page.

To log out, users click a logout button in the navigation bar. This logout button uses a POST form to securely end the user session and prevent unwanted logouts. After logging out, users see a confirmation page.

Behind the scenes, Django manages user sessions and uses CSRF protection to secure all POST requests, including logout. The URLs for login and logout use Django’s built-in views with custom templates for better user experience.

To test these features:

Register a new user and check that it creates an account.

Log in with valid credentials and verify access to the profile.

Try logging out by clicking the logout button and confirm you get the logged-out message.

Try to access the profile when logged out to confirm you get redirected to login.

