import simplejson
import ast
import datetime as dt
from datetime import datetime
import calendar

from django.core.urlresolvers import reverse
from django.views.generic.base import View
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# from attendance.models import Attendance, HolidayCalendar
# from college.models import Batch
# from academic.models import Student

class AddAttendance(View):

    def get(self, request, *args, **kwargs):

        current_date = datetime.now()
        context = {
            'current_date': current_date.strftime('%d/%m/%Y')
        }
        return render(request, 'attendance/add_attendance.html', {})

    def post(self, request, *args, **kwargs):

        status = 200       
        batch_details = ast.literal_eval(request.POST['batch'])
        day = request.POST['current_date']
        month = request.POST['current_month']
        year = request.POST['current_year']
        students = ast.literal_eval(request.POST['students'])
        batch = Batch.objects.get(id=batch_details['batch_id'])
        for student_details in students:    
            presented = []       
            student = Student.objects.get(id=student_details['student_id'])
            periods = student_details['counts']
            date = dt.date(int(year), int(month), int(day))
            print date
            attendance, created = Attendance.objects.get_or_create(batch=batch, student=student, date=date)
            attendance.presented = []   
            periods_present = 0         
            for period_details in periods:               
                if period_details['is_presented'] == 'true':
                    presented.append({
                        'period': period_details['count'],
                        'is_presented': True,
                        })   
                    periods_present = periods_present+1
                elif period_details['is_presented'] == 'false':
                    presented.append({
                        'period': period_details['count'],
                        'is_presented': False,
                        }) 
                    periods_present = periods_present-1
            if periods_present == int(batch.periods):
                attendance.status = "P"
            elif periods_present == -int(batch.periods):
                attendance.status = "A"
            else:
                attendance.status = "H"
            attendance.presented = presented
            attendance.save()                

        res = {
            'result': 'ok',
        }
        response = simplejson.dumps(res)
        return HttpResponse(response, status=status,  mimetype='application/json')

class BatchAttendanceList(View):

    def get(self, request, *args, **kwargs):

        batches = Batch.objects.all()
        ctx_batch = []
        status = 200
        current_date = datetime.now()
        year = current_date.year
        month = current_date.month      
        day = current_date.day  
        period_nos = []
        
        if request.is_ajax():
            for batch in batches:
                student_list = []                
                students = Student.objects.filter(batch=batch).order_by('roll_number')
                holiday_calendar = None
                for student in students:
                    period_list = []
                    date = dt.date(int(year), int(month), int(day))
                    holiday_calendar, created = HolidayCalendar.objects.get_or_create(date=date)
                    if created:
                        if date.strftime("%A") == 'Sunday' :
                            holiday_calendar.is_holiday = True             
                        holiday_calendar.save()
                    periods = int(batch.periods)
                    try:
                        attendance = Attendance.objects.get(date=date, student=student, batch=batch)
                        for period in attendance.presented:                          
                            period_list.append({
                            'count': period['period'],
                            'is_presented': 'true' if period['is_presented'] else 'false',
                            'is_holiday': 'true' if holiday_calendar and holiday_calendar.is_holiday else 'false',
                            'status': 'P' if period['is_presented'] else 'A',
                            })
                    except:                        
                        for period in range(1, periods + 1):                   
                            period_list.append({
                            'count': period,
                            'is_presented': "true",
                            'is_holiday': 'true' if holiday_calendar and holiday_calendar.is_holiday else 'false',
                            'status': '',
                            })
                    student_list.append({
                        'student_id': student.id,
                        'name': student.student_name,  
                        'roll_no': student.roll_number,
                        'counts': period_list          
                    })
                    period_list = []
                periods = int(batch.periods)   
                for period in range(1, periods + 1):
                    period_nos.append(period)              
                ctx_batch.append({
                    'batch_id': batch.id,
                    'name': str(batch.start_date) + '-' + str(batch.end_date) + ' ' + (str(batch.branch) if batch.branch else batch.course.course),
                    'course': batch.course.course if batch.course else '',
                    'periods': batch.periods,
                    'period_nos':period_nos,
                    'students': student_list,                          
                })
                period_nos = []
            res = {
                'batches': ctx_batch,
                'current_month': current_date.month,  
                'current_date': current_date.day,    
                'current_year': current_date.year, 
                'is_holiday': 'true' if holiday_calendar and holiday_calendar.is_holiday else 'false',  
                'result': 'ok',
            }
            response = simplejson.dumps(res)
            return HttpResponse(response, status=status, mimetype='application/json')



class AttendanceDetails(View):

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            status = 200
            batch =  Batch.objects.get(id=request.GET.get('batch_id', ''))
            student_list = []
            ctx_batch = []
            period_nos = []
            day_details = []
            holiday_calendar = None
            year = request.GET.get('batch_year', '')
            month = request.GET.get('batch_month', '')
            current_date = datetime.now()
            if(request.GET.get('batch_day')):
                day = request.GET.get('batch_day')
                students = Student.objects.filter(batch=batch).order_by('roll_number')
                for student in students:
                    day_details = []
                    period_list = []
                    date = dt.date(int(year), int(month), int(day))
                    holiday_calendar, created = HolidayCalendar.objects.get_or_create(date=date)
                    if created:
                        if date.strftime("%A") == 'Sunday' :
                            holiday_calendar.is_holiday = True             
                        holiday_calendar.save()
                    periods = int(batch.periods)
                    try:
                        attendance = Attendance.objects.get(date=date, student=student, batch=batch)
                        for period in attendance.presented:                          
                            period_list.append({
                            'count': period['period'],
                            'is_presented': 'true' if period['is_presented'] else 'false',
                            'is_future_date': "false",
                            'is_holiday': 'true' if holiday_calendar and holiday_calendar.is_holiday else 'false',
                            'status': 'P' if period['is_presented'] else 'A',
                            })
                    except:
                        for period in range(1, periods + 1):                   
                            period_list.append({
                            'count': period,
                            'is_presented': "true",
                            'is_future_date': "true" if datetime(int(year),int(month),int(day)) > datetime.now() else "false",
                            'is_holiday': 'true' if holiday_calendar and holiday_calendar.is_holiday else 'false',
                            'status': '',
                            })
                    student_list.append({
                        'student_id': student.id,
                        'name': student.student_name, 
                        'roll_no': student.roll_number, 
                        'counts': period_list          
                    })
                    period_list = []
                periods = int(batch.periods)   
                for period in range(1, periods + 1):
                    period_nos.append(period)     
                day_details.append({
                    'current_month': month,  
                    'current_date': day,    
                    'current_year': year,  
                    'is_future_date': "true" if datetime(int(year),int(month),int(day)) > datetime.now() else "false",
                    'is_holiday': 'true' if holiday_calendar and holiday_calendar.is_holiday else 'false',       
                    })         
                ctx_batch.append({
                    'batch_id': batch.id,
                    'name': str(batch.start_date) + '-' + str(batch.end_date) + ' ' + (str(batch.branch) if batch.branch else batch.course.course),
                    'course': batch.course.course if batch.course else '',                    
                    'column_count':period_nos,
                    'students': student_list,
                    'day_details': day_details,                   
                })             
                period_nos = []               
            else:  
                students = Student.objects.filter(batch=batch).order_by('roll_number')
                no_of_days = calendar.monthrange(int(year), int(month))[1]            
                calendar_days = []
                for day in range(1, no_of_days + 1):
                    calendar_days.append(day)
                for student in students:
                    days = []
                    for day in range(1, no_of_days + 1):
                        
                        date = dt.date(int(year), int(month), int(day))

                        holiday_calendar, created = HolidayCalendar.objects.get_or_create(date=date)

                        if created:
                            if date.strftime("%A") == 'Sunday' :
                                holiday_calendar.is_holiday = True             
                        holiday_calendar.save()

                        if not request.user.is_superuser:
                            is_future_date = 'true'
                        else:
                            is_future_date = 'false'
                        try:
                            attendance = Attendance.objects.get(date=date, student=student, batch=batch)
                            days.append({
                                'count': day,
                                'is_presented': "false" if attendance.status == "A" else "true",                      
                                'is_future_date': "true" if datetime(int(year),int(month),int(day)) > datetime.now() else "false",
                                'is_holiday': 'true' if holiday_calendar and holiday_calendar.is_holiday else 'false',
                                'status': attendance.status,
                            })
                        except:
                            days.append({
                                'count': day,
                                'is_presented': "true",
                                'is_future_date': "true" if datetime(int(year),int(month),int(day)) > datetime.now() else "false",
                                'is_holiday': 'true' if holiday_calendar and holiday_calendar.is_holiday else 'false',
                                'status': '',
                            })     
                    student_list.append({
                        'student_id': student.id,
                        'name': student.student_name,
                        'roll_no': student.roll_number,
                        'counts': days,
                    })
                ctx_batch.append({
                    'batch_id': batch.id,
                    'name': str(batch.start_date) + '-' + str(batch.end_date) + ' ' + (str(batch.branch) if batch.branch else batch.course.course),
                    'course': batch.course.course if batch.course else '',
                    'students': student_list,
                    'column_count': calendar_days,                   
                })
            res = {
                'batch': ctx_batch,
                'result': 'ok',
            }
            response = simplejson.dumps(res)
            return HttpResponse(response, status=status, mimetype='application/json')

        return render(request, 'attendance/attendance_details.html', {})

 


class ClearBatchAttendanceDetails(View):

    def get(self, request, *args, **kwargs):

        batch_id = request.GET.get('batch_id', '')
        batch_year = request.GET.get('batch_year', '')
        batch_month = request.GET.get('batch_month', '')
        if batch_id:
            batch = Batch.objects.get(id=batch_id)
            print batch_id, batch_year,batch_month
            attendance = Attendance.objects.filter(batch=batch, date__month=batch_month, date__year=batch_year)
            print attendance
            for attendance_obj in attendance:
                attendance_obj.delete()

            return HttpResponseRedirect(reverse('attendance_details'))
        return render(request, 'attendance/clear_batch_details.html', {})

class HolidayCalendarView(View):

    def get(self, request, *args, **kwargs):

        if request.is_ajax():

            status = 200
            year = request.GET.get('year', '')
            month = request.GET.get('month', '')

            no_of_days = calendar.monthrange(int(year), int(month))[1]
            
            calendar_days = []

            for day in range(1, no_of_days + 1):
                date = dt.date(int(year), int(month), int(day))
                
                holiday_calendar, created = HolidayCalendar.objects.get_or_create(date=date)
                if created:
                    if date.strftime("%A") == 'Sunday' :
                        holiday_calendar.is_holiday = True             
                holiday_calendar.save()
                
                calendar_days.append({
                    'day': day,
                    'is_holiday': "true" if holiday_calendar and holiday_calendar.is_holiday else "false",
                    'status': "H" if holiday_calendar and holiday_calendar.is_holiday else "W",
                })
            res = {
                'days': calendar_days,
            }

            response = simplejson.dumps(res)

            return HttpResponse(response, status=status, mimetype='application/json')

        return render(request, 'attendance/holiday_calendar.html', {})

    def post(self, request, *args, **kwargs):

        if request.is_ajax():

            year = request.POST['year']
            month = request.POST['month']

            status = 200

            holiday_calendar_details = ast.literal_eval(request.POST['holiday_calendar'])
            
            for details in holiday_calendar_details:
                date = dt.date(int(year), int(month), int(details['day']))

                holiday_calendar, created = HolidayCalendar.objects.get_or_create(date=date)

                if details['is_holiday'] == 'true':
                    holiday_calendar.is_holiday = True
                else:
                    holiday_calendar.is_holiday = False

                holiday_calendar.save()

            res = {
                'result': 'ok'
            }  
            response = simplejson.dumps(res)

            return HttpResponse(response, status=status, mimetype='application/json')

class ClearHolidayCalendar(View):

    def get(self, request, *args, **kwargs):

        year = request.GET.get('year', '')
        month = request.GET.get('month', '')
        status = 200
        if year and month:
            holiday_calendar = HolidayCalendar.objects.filter(date__year=year, date__month=month)

            for calendar in holiday_calendar:

                calendar.delete()

            res = {
                'result': 'ok',
            }
            response = simplejson.dumps(res)
            return HttpResponseRedirect(reverse('clear_holiday_calendar'))
        return render(request, 'attendance/clear_holiday_calendar.html', {})





