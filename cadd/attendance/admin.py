from django.contrib import admin
from attendance.models import *

admin.site.register(Attendance)
admin.site.register(HolidayCalendar)
admin.site.register(StudentAttendance)
