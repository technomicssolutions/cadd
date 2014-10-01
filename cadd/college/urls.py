
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from college.views import Softwares, DeleteSoftware, Courses 

urlpatterns = patterns('',
	url(r'^softwares/$',login_required (Softwares.as_view()), name='softwares'),
	url(r'^delete_software/(?P<software_id>\d+)/$',login_required (DeleteSoftware.as_view()), name='delete_software'),
	
	url(r'^courses/$',login_required (Courses.as_view()), name='courses'),
)