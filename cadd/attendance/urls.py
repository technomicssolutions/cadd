from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from attendance.views import AddAttendance, BatchAttendanceList, AttendanceDetails, ClearBatchAttendanceDetails, \
	HolidayCalendarView, ClearHolidayCalendar, BatchStudents

urlpatterns = patterns('',
	url(r'^batch_students/(?P<batch_id>\d+)/$',login_required (BatchStudents.as_view()), name="batch_students"),

	url(r'^add_attendance/$',login_required(AddAttendance.as_view()), name='add_attendance'),
	#url(r'^batches/$',login_required(BatchAttendanceList.as_view()), name='batches'),
	url(r'^attendance_details/$',login_required(AttendanceDetails.as_view()), name='attendance_details'),
	url(r'^clear_batch_details/$',login_required(ClearBatchAttendanceDetails.as_view()), name='clear_batch_details'),
	
	url(r'^holiday_calendar/$',login_required(HolidayCalendarView.as_view()), name='holiday_calendar'),
	url(r'^clear_holiday_calendar/$', login_required(ClearHolidayCalendar.as_view()), name='clear_holiday_calendar'),

)