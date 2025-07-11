retrieved = Book.objects.get(id=book.id)
print(retrieved.title, retrieved.author, retrieved.publication_year)
# Output: 1984 George Orwell 1949
