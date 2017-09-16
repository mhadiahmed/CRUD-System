from django import forms
from .models import Book

class BookForm(forms.ModelForm):
	publication_date = forms.DateTimeInput()
	class Meta:
		model = Book
		fields = ('title', 'publication_date', 'author', 'price', 'pages', 'book_type', )