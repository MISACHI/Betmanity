from django.conf.urls import url
from .views import (
	index,
	placement,
	register,
	log_in,
	contact,
	)

urlpatterns = [
	url(r'^$', index, name='bet_index'),
    url(r'^place/$', placement, name='bet_place'),
    url(r'^register/$', register, name='bet_register'),
    url(r'^log_in/$', log_in, name='bet_login'),
    url(r'^contact/$', contact, name='bet_contact'),
]