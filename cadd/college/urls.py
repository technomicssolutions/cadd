
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from college.views import ListSoftwares,DeleteSoftware, ListBatch, AddNewBatch, EditBatch

urlpatterns = patterns('',
	url(r'^softwares/$',login_required (ListSoftwares.as_view()), name='softwares'),
	url(r'^delete_software/(?P<software_id>\d+)/$',login_required (DeleteSoftware.as_view()), name='delete_software'),
	url(r'^batches/$',login_required (ListBatch.as_view()), name='batch_list'),
	url(r'^add_new_batch/$',login_required (AddNewBatch.as_view()), name='add_new_batch'),
	url(r'^edit_batch/(?P<batch_id>\d+)/$',login_required (EditBatch.as_view()), name="edit_batch"),


)