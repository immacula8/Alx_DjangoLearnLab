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

##Adding Comment Functionality to Blog Posts##

I started by making sure my blog could actually store comments.
The first thing I did was create a Comment model in models.py. This model was connected to my Post model with a ForeignKey, which means every comment belongs to a specific post. I also added fields like author, text, and created_at so that each comment could store who wrote it, what they wrote, and when.

Once the model was ready, I created a CommentForm in forms.py. This form made it easy for users to type and submit comments without manually handling raw HTML forms. It was linked to our Comment model so that when a user submitted a comment, it could be saved directly to the database.

Next, I updated my post_detail view. This view was in charge of showing a single blog post, and now I made it handle both displaying existing comments and saving new ones. Inside the view, I first retrieved the post and its related comments. Then, if the request was a POST (meaning a form was submitted), I checked if the form was valid, assigned the comment to the post and the logged-in user, and saved it. If it wasn’t a POST request, I just showed the empty form.

After the view was ready, I moved to the template post_detail.html and added two things:

A section to display all existing comments for the post.

A comment submission form for logged-in users.

Once everything was wired up, I ran migrations to update the database so it could store comments. Then, I went into the Django admin panel. But before I could see or manage comments there, I had to register my Comment model in admin.py. This allowed the admin interface to show all submitted comments, so I could approve, edit, or delete them from the backend.

Finally, I tested it:
I opened a post, typed a comment, submitted it, and saw it appear instantly on the post’s page. Then, I confirmed in the admin panel that the comment was saved correctly and linked to the right post. Everything worked — both frontend display and backend management.

##Implementing Advanced Features: Tagging and Search Functionality##

In this update to my blog application, I integrated tagging functionality, improved post creation and update forms, and configured URLs to support tag-based navigation. These changes enhance both the content management process for authors and the browsing experience for readers.

To begin, I enabled the django-taggit library by adding "taggit" to the INSTALLED_APPS list in my settings.py file. This library provides a simple and flexible way to add tags to models without having to manually implement a tagging system from scratch. I then updated my Post model to include a tags field using TaggableManager. This allows each blog post to have one or more tags, which can later be used to filter and organize posts by topics.

Next, I modified the post creation and update forms in forms.py to include tag input. To make the tagging experience more user-friendly, I used TagWidget from taggit and specified it in the form’s Meta class using the widgets dictionary. This ensures that when creating or editing a post, I can easily add tags in a clean and intuitive input field.

I also worked on the URL configuration to support browsing posts by specific tags. In urls.py, I added a new path, tags/<slug:tag_slug>/, and connected it to a PostByTagListView class-based view. This view retrieves posts that match a given tag slug, allowing readers to click on a tag and instantly see all related posts.

Finally, I updated the templates to display tags on the post list and detail pages, and I made sure that each tag is clickable, leading to its filtered list view. This improvement not only organizes content better but also increases engagement by helping readers explore related topics.

With these changes, my blog now supports tagging in a seamless way, making content easier to find and giving authors a better workflow for categorizing their posts.