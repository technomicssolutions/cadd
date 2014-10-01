
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from college.views import ListSoftwares

urlpatterns = patterns('',
	url(r'^list_softwares/$',login_required (ListSoftwares.as_view()), name='list_softwares'),
	
)