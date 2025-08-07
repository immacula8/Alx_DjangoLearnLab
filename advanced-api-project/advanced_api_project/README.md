## 📚 API Features: Filtering, Searching, and Ordering

### 🔍 Filtering

You can filter books by:

- `title`
- `author` (author ID)
- `publication_year`

### 🔎 Search

You can search books by `title` or `author name`.

### ⬇️ Ordering

Order books by:

- `title`
- `publication_year`

**Examples:**

- Ascending: `?ordering=title`
- Descending: `?ordering=-publication_year`


---

### 🔐 Notes on Permissions

These features are protected:
- Only authenticated users can create books.
- Anyone can read/list books.

The Documentation of the test:

1. Testing Strategy
We use Django REST Framework’s APITestCase to test our API endpoints.
Our goal is to:

Check if API endpoints work correctly (create, read, update, delete).

Ensure authentication and permissions are enforced.

Verify that the database updates correctly after each request.

2. Test Cases
a) Create a Book
Purpose: Check if a new book can be created.

Steps:

Send a POST request to /api/books/ with book details.

Verify response status is 201 Created.

Check the database to confirm the book was added.

b) List Books
Purpose: Check if all books can be retrieved.

Steps:

Send a GET request to /api/books/.

Verify response status is 200 OK.

Check that returned data matches books in the database.

c) Update a Book
Purpose: Check if a book’s details can be updated.

Steps:

Send a PUT/PATCH request to /api/books/{id}/ with updated info.

Verify response status is 200 OK.

Check the database to confirm the changes were saved.

d) Delete a Book
Purpose: Check if a book can be deleted.

Steps:

Send a DELETE request to /api/books/{id}/.

Verify response status is 204 No Content.

Check that the book is removed from the database.

e) Authentication & Permissions
Purpose: Ensure only authenticated users can create, update, or delete books.

Steps:

Send requests without authentication.

Verify response status is 401 Unauthorized.

How to run the tests:
1. you can activate your virtual environment using (source env/bin/activate) and then run it using (python manage.py test api(api is the name of your app)).