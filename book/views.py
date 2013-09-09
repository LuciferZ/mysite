from django.shortcuts import render_to_response
from django.http import HttpResponse
from book.models import Book
def search_form(request):
	return render_to_response('search_form.html')
def search(request):
	errors = []
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			errors.append('Enter The search term')
		elif len(q) > 20:
			errors.append('Please enter at most 20 charactors')
		else:
			books = Book.objects.filter(title__contains=q)
			return render_to_response('search_result.html',
				{'books':books,'query':q})
	else:
		errors = True
	return render_to_response('search_form.html',{'errors': errors})
	