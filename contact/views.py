from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.core.context_processors import csrf

def contact(request):
	errors = []
	if request.method == 'POST':
		if not request.POST.get('subject', ''):
			errors.append('Please Enter a subject:')
		if not request.POST.get('message', ''):
			errors.append('Please Enter a message:')
		if request.POST.get('email') and '@' not in request.POST['email']:
			errors.append('Please Enter a valid email address.')
		if not errors:
			# send_mail(
			# 	request.POST['subject'],
			# 	request.POST['message'],
			# 	request.POST.get('email','zyzhang@iflytek.com'),
			# 	['zyzhang@iflytek.com'],
			# 	)
			return HttpResponseRedirect('/contact/thanks/')
		return render_to_response('contact_form.html',
			{'errors':errors})
	else:
		return render_to_response("contact_form.html")
def thanks(request):
	return HttpResponse("thanks")