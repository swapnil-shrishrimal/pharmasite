import os
from django.shortcuts import render
from django.core.mail import send_mail
from django.template.context_processors import csrf
# Create your views here.
#Home page view
def home(request):
	return render(request, 'home.html', {})


#Contact page view
def contact(request):
	if request.method == "POST":
		name = request.POST['name']
		email = request.POST['email']
		message = request.POST['message']
		c = {}
		c.update(csrf(request))

		#Email code here
		send_mail(
			'Email from ' + name, # subject
			message, # message
			email, # from email
			['rishabhtathed3103@gmail.com','indiconinnovatives1998@gmail.com'], # to email
			auth_user = os.environ['EMAIL_HOST_USER'],
			auth_password = os.environ['EMAIL_HOST_PASSWORD'],
			fail_silently = False,
			)

		return render(request, 'contact.html', {'name' : name})

	else:
		return render(request, 'home.html', {})