from django.core.management.base import BaseCommand
from BetApp.models import Login_detail, Team, Customer_placement

class Command(BaseCommand):
	args = '<foo bar ...>'
	help = 'our help string comes here'

	def _create_Team(self):
		t1 = Team(Ateams='Arsenal',Bteams='Man Utd',Draw=3.3,A_odds=1.3,B_odds=4.5)
		t1.save()

		t2 = Team(Ateams='Chelsea',Bteams='Leeds Utd',Draw=4.5,A_odds=4.1,B_odds=7.5)
		t2.save()

		t3 = Team(Ateams='Cavaliers',Bteams='OKC',Draw=2.3,A_odds=1.3,B_odds=3.5)
		t3.save()

		t4 = Team(Ateams='Knicks',Bteams='Bulls',Draw=2.3,A_odds=3.3,B_odds=1.5)
		t4.save()

		t5 = Team(Ateams='Miami',Bteams='GSW',Draw=2.3,A_odds=4.7,B_odds=1.1)
		t5.save()

		t6 = Team(Ateams='Lakers',Bteams='Wizards',Draw=3.4,A_odds=2.6,B_odds=3.5)
		t6.save()


	def handle(self, *args, **options):
		self._create_Team()