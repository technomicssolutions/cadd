
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from college.views import ListSoftwares,DeleteSoftware

urlpatterns = patterns('',
	url(r'^softwares/$',login_required (ListSoftwares.as_view()), name='softwares'),
	url(r'^delete_software/(?P<software_id>\d+)/$',login_required (DeleteSoftware.as_view()), name='delete_software'),
	

)