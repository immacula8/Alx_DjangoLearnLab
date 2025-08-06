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

