from django.shortcuts import render
from django.core.mail import send_mail

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

		#Email code here
		send_mail(
			'Email from ' + name, # subject
			message, # message
			email, # from email
			['shrishrimalswapnil@gmail.com','indiconinnovatives1998@gmail.com'], # to email
			auth_user = 'indiconinnovatives1998@gmail.com',
			auth_password = '',
			fail_silently = False,
			)

		return render(request, 'contact.html', {'name' : name})

	else:
		return render(request, 'home.html', {})