from django import forms
from django.db import models
from django.contrib.auth.models import User

from BetApp.models import Support, Login_detail

class SigninForm(forms.ModelForm):
	password2 = forms.CharField(
		label = 'Password Confirmation',
		widget=forms.PasswordInput(attrs={
			'class':'form-control',
			'placeholder':'Confirm password',
			'name':'password2',
		}),
	)

	def clean(self):
		password = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('password2')

		if not password2:
			raise forms.ValidationError('You must Confirm Your password')

		if password != password2:
			raise forms.ValidationError('Your passwords Do not match!')
			return password2

	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'email', 'password', 'password2']
		widgets = {
			'username':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Username',
			}),
			'email':forms.EmailInput(attrs={
				'class':'form-control',
				'placeholder':'Email address',
			}),
			'first_name':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'First name here',
			}),
			'last_name':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Last name here',
			}),
			'password':forms.PasswordInput(attrs={
				'class':'form-control',
				'placeholder':'Password',
				'name':'password'})
		}

class SupportForm(forms.ModelForm):
	email = forms.EmailField(
			label = 'Email Address',
			widget = forms.TextInput({
				'class': 'form-control',
				'placeholder': 'Email',
				'name': 'email',
			}),
		)
	location = forms.CharField(
			label = 'Location',
			widget = forms.TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'location',
				'name' : 'location',
			}),
		)
	brief_description = forms.CharField(
			label = 'Brief description',
			widget = forms.TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Brief description',
				'name': 'brief_description'
			}),
		)
	full_description = forms.CharField(
			label = 'Full description',
			widget = forms.Textarea(attrs={
				'class': 'form-control',
				'placeholder': 'Full description',
				'name': 'full_description',
			}),
		)

	class Meta:
		model = Support
		fields = ['email', 'location', 'brief_description', 'full_description']

	