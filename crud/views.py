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
	data = dict()
	if request.method == 'POST':
		form = BookForm(request.POST)
		if form.is_valid():
			form.save()
			data['form_is_valid'] = True
			books = Book.objects.all()
			data['book_list'] = render_to_string('book_list_2.html',{'books':books})
		else:
			data['form_is_valid'] = False
	else:
		form = BookForm()
	context = {
	'form':form
	}
	data['html_form'] = render_to_string('book_create.html',context,request=request)
	return JsonResponse(data)










	



	

