from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from BetApp.models import Login_detail, Customer_placement, Team, Support
from BetApp.forms import SigninForm, SupportForm

def index(request):
	teams = Team.objects.all()
	choices = {
		'first': teams[:20],
		'second': teams[20:40],
		'third': teams[40:60],
	}
	content = {
		'teams' : teams,
		'choices': choices,
	}
			
	return render(request, 'BetApp/home.html', content)

def placement(request):
	if request.method == 'POST':
		team = request.POST['team']
		if request.user.is_authenticated:
			name = request.user
			bet = Customer_placement()
			bet.customer_name = name
			bet.selected_team = team
			bet.save()

	return HttpResponse('')

def log_in(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/bet/')
			else:
				return HttpResponse('Your account is disabled.')
		else:
			print('Invalid login details:{0}, {1}'.format(username, password))
			return HttpResponse('Invalid login Details supplied')

	return render(request, 'BetApp/signin.html', {})

def register(request):
	if request.method == 'POST':
		user_form = SigninForm(request.POST)
		if user_form.is_valid():
			user = user_form.save(commit=False)
			user.set_password(user.password)
			user.save()
			return HttpResponseRedirect('/bet/')
		else:
			return render(request, 'BetApp/register.html', {'form' : user_form})
	else:
		user_form = SigninForm()

	return render(request, 'BetApp/register.html', {'form' : user_form})

def contact(request):
	if request.method == 'POST':
		support_details = SupportForm(request.POST)
		if support_details.is_valid():
			support_details.save(commit=True)
			return HttpResponseRedirect('/bet/')
		else:
			return render(request, 'BetApp/contact-us.html', {'form': support_details})
	else:
		support_details = SupportForm()

	return render(request, 'BetApp/contact-us.html', {'form': support_details})