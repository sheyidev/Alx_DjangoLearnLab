book = Book.objects.create(title="1984",author="George Orwell",publication_year=1949)

retrieved_book=Book.objects.get(title="1984")
