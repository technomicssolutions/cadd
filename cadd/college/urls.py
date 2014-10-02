
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from college.views import Softwares,DeleteSoftware, Courses, ListBatch, AddNewBatch, EditBatch, \
	DeleteCourse, DeleteBatch, CourseDetails


urlpatterns = patterns('',
	url(r'^softwares/$',login_required (Softwares.as_view()), name='softwares'),
	url(r'^delete_software/(?P<software_id>\d+)/$',login_required (DeleteSoftware.as_view()), name='delete_software'),
	url(r'^courses/$',login_required (Courses.as_view()), name='courses'),
	url(r'^delete_course/(?P<course_id>\d+)/$',login_required (DeleteCourse.as_view()), name='delete_course'),
	url(r'^course_details/$',login_required (CourseDetails.as_view()), name='course_details'),
	url(r'^batches/$',login_required (ListBatch.as_view()), name='batch_list'),
	url(r'^add_new_batch/$',login_required (AddNewBatch.as_view()), name='add_new_batch'),
	url(r'^edit_batch/(?P<batch_id>\d+)/$',login_required (EditBatch.as_view()), name="edit_batch"),
	url(r'^delete_batch/(?P<batch_id>\d+)/$',login_required (DeleteBatch.as_view()), name="delete_batch"),


)