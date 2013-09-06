from django.shortcuts import render_to_response
from django.http import HttpResponse
from book.models import Book
def search_form(request):
	return render_to_response('search_form.html')
def search(request):
	if 'q' in request.GET and request.GET['q']:
		q = request.GET['q']
		books = Book.objects.filter(title__contains=q)
		return render_to_response('search_result.html',
			{'books':books,'query':q})
	else:
		return render_to_response('search_form.html',{'error': True})
	