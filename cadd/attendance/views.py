import simplejson
import ast
import datetime as dt
from datetime import datetime
import calendar

from django.core.urlresolvers import reverse
from django.views.generic.base import View
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from attendance.models import Attendance, HolidayCalendar, StudentAttendance
from college.models import Batch
from admission.models import Student
from staff.models import Staff

class AddAttendance(View):

    def get(self, request, *args, **kwargs):

        current_date = datetime.now()
        context = {
            'current_date': current_date.strftime('%d/%m/%Y')
        }
        print current_date
        return render(request, 'add_attendance.html', context)

    def post(self, request, *args, **kwargs):

        status = 200       
        day = request.POST['current_date']
        month = request.POST['current_month']
        year = request.POST['current_year']
        students = ast.literal_eval(request.POST['students'])
        batch_details = ast.literal_eval(request.POST['batch'])
        batch = Batch.objects.get(id=batch_details['id'])
        user = request.user;
        date = dt.date(int(year), int(month), int(day))
        try:
            attendance = Attendance.objects.get(batch=batch, date=date)
        except:
            attendance = Attendance()
            attendance.batch = batch
            attendance.date = date
        attendance.user = user
        attendance.topics_covered =  batch_details['topics']
        if batch_details['remarks']:
            attendance.remarks = batch_details['remarks']
        attendance.save()
        for student_details in students:    
            student = Student.objects.get(id=student_details['id'])
            student_attendance, created =  StudentAttendance.objects.get_or_create(student=student, attendance=attendance)
            if student_details['is_presented'] == 'true':
                student_attendance.status = "P"
            else:
                student_attendance.status = "A"
            student_attendance.save()                
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
        return HttpResponse('Ok')



class AttendanceDetails(View):

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            status = 200
            batch =  Batch.objects.get(id=request.GET.get('batch_id', ''))
            student_list = []
            ctx_batch = []
            period_nos = []
            day_details = []
            day_list = []
            batch_list = []
            holiday_calendar = None
            year = request.GET.get('batch_year', '')
            month = request.GET.get('batch_month', '')
            current_date = datetime.now()
            if(request.GET.get('batch_day')):
                day = request.GET.get('batch_day')
                students = batch.student_set.all().order_by('roll_number')
                students_list = []
                date = dt.date(int(year), int(month), int(day))
                try:
                    attendance = Attendance.objects.get(batch=batch, date=date)
                    if attendance.user.username == 'admin':
                        staff = attendance.user.username
                    else:
                        staff_obj = Staff.objects.get(user=attendance.user)
                        staff = staff_obj.user.first_name + " " + staff_obj.user.last_name
                except Exception as ex:
                    print str(ex)
                    attendance = Attendance()
                    staff = ''
                for student in students:
                    try:
                        student_attendance = StudentAttendance.objects.get(attendance=attendance, student=student)
                    except:
                        student_attendance = StudentAttendance()
                    students_list.append({
                        'id': student.id,
                        'name': student.student_name,
                        'roll_number': student.roll_number,
                        'status': student_attendance.status if student_attendance.status else 'NA',
                        'is_presented': 'false' if student_attendance.status == 'A' else 'true',
                    })
                res = {
                    'batch_id': batch.id,
                    'students': students_list,
                    'current_month': current_date.month,  
                    'current_date': current_date.day,    
                    'current_year': current_date.year, 
                    'topics': attendance.topics_covered if attendance.topics_covered else '',
                    'remarks': attendance.remarks if attendance.remarks else '',
                    'staff': staff,
                    'view': 'daily',
                    'is_future_date': "true" if datetime(int(year),int(month),int(day)) > datetime.now() else "false",
                }            
            else:  
                students = batch.student_set.all().order_by('roll_number')
                no_of_days = calendar.monthrange(int(year), int(month))[1]            
                calendar_days = []
                for day in range(1, no_of_days + 1):
                    calendar_days.append(day)
                for student in students:
                    for day in range(1, no_of_days + 1):       
                        date = dt.date(int(year), int(month), int(day))
                        try:
                            attendance = Attendance.objects.get(date=date, batch=batch)
                        except:
                            attendance = Attendance()
                        try:
                            student_attendance = StudentAttendance.objects.get(attendance=attendance, student=student)
                        except:
                            student_attendance = StudentAttendance()
                        day_list.append({
                            'count': day,
                            'status': student_attendance.status if student_attendance.status else '',
                            'is_future_date': "true" if datetime(int(year),int(month),int(day)) > datetime.now() else "false",
                            })
                    student_list.append({
                        'id': student.id,
                        'name': student.student_name,
                        'roll_number': student.roll_number,
                        'days': day_list,
                        })
                    day_list = []
                batch_list.append({
                    'students': student_list,
                    'column_count': calendar_days,
                    })
                res = {
                    'batch': batch_list,
                    'result': 'ok',
                    'view': 'monthly',
                }
            response = simplejson.dumps(res)
            return HttpResponse(response, status=status, mimetype='application/json')

        return render(request, 'attendance_details.html', {})


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


class BatchStudents(View):

    def get(self, request, *args, **kwargs):

        current_date = datetime.now()
        year = current_date.year
        month = current_date.month      
        day = current_date.day  
        batch_id = kwargs['batch_id']
        batch = Batch.objects.get(id=batch_id)
        students = batch.student_set.all().order_by('roll_number')
        students_list = []
        date = dt.date(int(year), int(month), int(day))
        try:
            attendance = Attendance.objects.get(batch=batch, date=date)
            if attendance.user.username == 'admin':
                staff = attendance.user.username
            else:
                staff_obj = Staff.objects.get(user=attendance.user)
                staff = staff_obj.user.first_name + " " + staff_obj.user.last_name
        except Exception as ex:
            print str(ex)
            attendance = Attendance()
            staff = ''
        for student in students:
            try:
                student_attendance = StudentAttendance.objects.get(attendance=attendance, student=student)
            except:
                student_attendance = StudentAttendance()
            students_list.append({
                'id': student.id,
                'name': student.student_name,
                'roll_number': student.roll_number,
                'status': student_attendance.status if student_attendance.status else 'NA',
                'is_presented': 'false' if student_attendance.status == 'A' else 'true',
            })
        res = {
            'students': students_list,
            'current_month': current_date.month,  
            'current_date': current_date.day,    
            'current_year': current_date.year, 
            'topics': attendance.topics_covered if attendance.topics_covered else '',
            'remarks': attendance.remarks if attendance.remarks else '',
            'staff': staff,
        }
        status_code = 200
        response = simplejson.dumps(res)
        return HttpResponse(response, status = status_code, mimetype="application/json")


class JobCard(View):

     def get(self, request, *args, **kwargs):

        return render(request, 'job_card.html', {})



