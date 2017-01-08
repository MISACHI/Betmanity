from django.db import models
from django.contrib.auth.models import User

class Login_detail(models.Model):
	customer_id = models.AutoField(primary_key=True)
	user = models.OneToOneField(User)

	def __str__(self):
		return self.user.first_name + '\t' + self.user.last_name

class Team(models.Model):
	team_id = models.AutoField(primary_key=True)
	customer_id = models.ForeignKey(Login_details, on_delete=models.CASCADE)
	Ateams = models.CharField(max_length=50)
	A_odds = models.FloatField()
	Draws = models.CharField(max_length=50)
	Draw = models.FloatField()
	Bteams = models.CharField(max_length=50)
	B_odds = models.FloatField()

	def __str__(self):
		return self.Ateams + '\t vs \t' + self.Bteams

class Customer_placement(models.Model):
	team_id = models.AutoField(primary_key=True)
	customer_name = models.CharField(max_length=50)
	selected_team = models.CharField(max_length=50)

	def __str__(self):
		return self.customer_name + '\t' + self.selected_team

class Support(models.Model):
	customer_id = models.AutoField(primary_key=True)
	email = models.EmailField()
	location = models.CharField(max_length=50)
	brief_description = models.CharField(max_length=50)
	full_description = models.CharField(max_length=300)

	def __str__(self):
		return self.brief_description +'\t from \t '+ self.email
