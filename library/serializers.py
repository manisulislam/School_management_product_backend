# academics/serializers.py (or library/serializers.py)
from rest_framework import serializers
from .models import Book, BookIssue

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookIssueSerializer(serializers.ModelSerializer):
    # Optional: display book title and student info in the response
    book_title = serializers.CharField(source='book.title', read_only=True)
    student_name = serializers.CharField(source='student.name', read_only=True)

    class Meta:
        model = BookIssue
        fields = ['id', 'book', 'book_title', 'student', 'student_name', 'issue_date', 'return_date', 'is_returned']
