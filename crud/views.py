from django.shortcuts import render
from .models import Book
from .forms import BookForm
from django.http import JsonResponse
from django.template.loader import render_to_string

def book_list(request):
	books = Book.objects.all()
	context = {
	'books': books
	}
	return render(request, 'book_list.html',context)

def book_create(request):
	form = BookForm()
	context = {
	'form':form
	}
	html_form = render_to_string('book_create.html',context,request=request)
	return JsonResponse({'html_form':html_form})










	



	

