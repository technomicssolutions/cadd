from django.conf.urls import patterns, include, url

from django.conf import settings
from django.contrib.auth.decorators import login_required

from web.views import Home, ResetPassword, Login, Logout, Letters, DeleteLetter

urlpatterns = patterns('',
	
	url(r'^$', Home.as_view(), name='home'),
	url(r'login/$',  Login.as_view(), name='login'),
    url(r'logout/$', Logout.as_view(), name='logout'),

	url(r'letters/$', Letters.as_view(), name='letters'),    
	url(r'^delete_letter/(?P<letter_id>\d+)/$',login_required (DeleteLetter.as_view()), name='delete_letter'),
    
    url(r'^reset_password/(?P<user_id>\d+)/$', login_required(ResetPassword.as_view()), name="reset_password"),
	
)