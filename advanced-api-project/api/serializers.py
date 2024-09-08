from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    #    Serializer for the Book model.

    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        if value > datetime.date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    #    Serializer for the Author model, including nested books.
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
