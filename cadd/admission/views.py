
import simplejson
import ast

from django.core.urlresolvers import reverse
from django.views.generic.base import View
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from admission.models import Student, Enquiry
from college.models import Course, Batch
from datetime import datetime

class AddStudent(View):
    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            try:
                course = Course.objects.get(id = request.POST['course'])
                batch = Batch.objects.get(id = request.POST['batch'])
                batch.no_of_students = batch.no_of_students + 1
                batch.save()
                student, created = Student.objects.get_or_create(roll_number = request.POST['roll_number'], course=course, batch=batch)
                if not created:
                    res = {
                        'result': 'error',
                        'message': 'Student with this roll no already existing'
                    }
                else:
                    try:
                        student.student_name = request.POST['student_name']
                        student.roll_number = request.POST['roll_number']
                        student.address = request.POST['address']
                        student.qualifications = request.POST['qualifications']
                        student.course=course
                        student.batch=batch
                        student.dob = datetime.strptime(request.POST['dob'], '%d/%m/%Y')
                        student.address = request.POST['address']
                        student.mobile_number = request.POST['mobile_number']
                        student.email = request.POST['email']
                        student.blood_group = request.POST['blood_group']
                        student.doj = datetime.strptime(request.POST['doj'], '%d/%m/%Y')
                        student.photo = request.FILES.get('photo_img', '')                       
                        student.certificates_submitted = request.POST['certificates_submitted']
                        student.certificates_remarks = request.POST['certificates_remarks']
                        student.id_proofs_submitted = request.POST['id_proofs_submitted']
                        student.guardian_name = request.POST['guardian_name']
                        student.relationship = request.POST['relationship']
                        student.guardian_mobile_number = request.POST['guardian_mobile_number']
                        student.is_rolled = True                 
                    except Exception as ex:
                        res = {
                            'result': 'error',
                            'message': str(ex)
                        }
                    student.save()
                    res = {
                        'result': 'ok',
                    }                     
            except Exception as ex:
                res = {
                    'result': 'error',
                    'message': str(ex)
                }
            status_code = 200 
            response = simplejson.dumps(res)
            return HttpResponse(response, status = status_code, mimetype="application/json")
        return render(request, 'list_student.html', {})

class ListStudent(View):
    def get(self, request, *args, **kwargs):
        if request.GET.get('batch_id', ''):
            students = Student.objects.filter(batch__id=request.GET.get('batch_id', '')).order_by('roll_number')
        else:
            students = Student.objects.all().order_by('roll_number')   
        if request.is_ajax():
            student_list = []
            for student in students:
                student_list.append({
                    'id': student.id,
                    'name': student.student_name,
                    'roll_number': student.roll_number,
                })            
            response = simplejson.dumps({
                'result': 'Ok',
                'students': student_list
            })
            return HttpResponse(response, status = 200, mimetype="application/json")
        ctx = {
            'students': students
        }
        return render(request, 'list_student.html',ctx)



class GetStudent(View):

    def get(self, request, *args, **kwargs):
        course_id = kwargs['course_id']
        batch_id = kwargs['batch_id']
        if request.is_ajax():
            try:
                students = Student.objects.filter(course__id=course_id, batch__id=batch_id)
                student_list = []
                for student in students:
                    student_list.append({
                        'student': student.student_name,
                        'id' :student.id 
                    })
                res = {
                    'result': 'ok',
                    'students': student_list,
                }
            except Exception as ex:
                res = {
                    'result': 'error: '+ str(ex),
                }
            status = 200
            response = simplejson.dumps(res)
            return HttpResponse(response, status=status, mimetype='application/json')

class ViewStudentDetails(View):  

    def get(self, request, *args, **kwargs):
        
        student_id = kwargs['student_id']
        ctx_student_data = []
        if request.is_ajax():
            try:
                student = Student.objects.get(id = student_id)
               
                ctx_student_data.append({
                'student_name': student.student_name if student.student_name else '',
                'roll_number': student.roll_number if student.roll_number else '',
                'dob': student.dob.strftime('%d/%m/%Y') if student.dob else '',
                'address': student.address if student.address else '',
                'course': student.course.id if student.course else '',
                'batch' :student.batch.id if student.batch else '',
                'mobile_number': student.mobile_number if student.mobile_number else '',
                'email': student.email if student.email else '',
                'blood_group': student.blood_group if student.blood_group else '',
                'doj': student.doj.strftime('%d/%m/%Y') if student.doj else '',
                'photo': student.photo.name if student.photo.name else '',
                'certificates_submitted': student.certificates_submitted if student.certificates_submitted else '',
                'id_proofs_submitted': student.id_proofs_submitted if student.id_proofs_submitted else '',
        
                'guardian_name': student.guardian_name if student.guardian_name else '',
                
                'relationship': student.relationship if student.relationship else '',
                'guardian_mobile_number': student.guardian_mobile_number if student.guardian_mobile_number else '',
                })
                res = {
                    'result': 'ok',
                    'student': ctx_student_data,
                }
            except Exception as ex:
                res = {
                    'result': 'error: ' + str(ex),
                    'student': ctx_student_data,
                }
            status = 200
            response = simplejson.dumps(res)
            return HttpResponse(response, status=status, mimetype='application/json')

class EditStudentDetails(View):
   
    def get(self, request, *args, **kwargs):
        
        student_id = kwargs['student_id']
        context = {
            'student_id': student_id,
        }
        ctx_student_data = []
        student = Student.objects.get(id=student_id)
        if request.is_ajax():
            ctx_student_data.append({
                'student_name': student.student_name if student.student_name else '',
                'roll_number': student.roll_number if student.roll_number else '',
                'dob': student.dob.strftime('%d/%m/%Y') if student.dob else '',
                'address': student.address if student.address else '',
                'course': student.course.id if student.course else '',
                'batch' :student.batch.id if student.batch else '',
                'mobile_number': student.mobile_number if student.mobile_number else '',
                'email': student.email if student.email else '',
                'blood_group': student.blood_group if student.blood_group else '',
                'doj': student.doj.strftime('%d/%m/%Y') if student.doj else '',
                'photo': student.photo.name if student.photo.name else '',
                'certificates_submitted': student.certificates_submitted if student.certificates_submitted else '',
                'id_proofs_submitted': student.id_proofs_submitted if student.id_proofs_submitted else '',
        
                'guardian_name': student.guardian_name if student.guardian_name else '',
                
                'relationship': student.relationship if student.relationship else '',
                'guardian_mobile_number': student.guardian_mobile_number if student.guardian_mobile_number else '',
        
                })
            res = {
                'result': 'ok',
                'student': ctx_student_data,
            }
            status = 200
            response = simplejson.dumps(res)
            return HttpResponse(response, status=status, mimetype='application/json')
        return render(request, 'edit_student_details.html',context)

    def post(self, request, *args, **kwargs):

        student_id = kwargs['student_id']
        student = Student.objects.get(id = student_id)
        student_data = ast.literal_eval(request.POST['student'])
        try:
            student.student_name = student_data['student_name']
            student.roll_number = student_data['roll_number']
            student.address = student_data['address']
            course = Course.objects.get(course = student_data['course'])
            student.course=course
            batch = Batch.objects.get(batch = student_data['batch'])
            student.batch=batch

            student.dob = datetime.strptime(student_data['dob'], '%d/%m/%Y')
            student.address = student_data['address']
            student.mobile_number = student_data['mobile_number']
            
            student.email = student_data['email']
            student.blood_group = student_data['blood_group']
            student.doj = datetime.strptime(student_data['doj'], '%d/%m/%Y')
            student.photo = request.FILES.get('photo_img', '')                       
            student.certificates_submitted = student_data['certificates_submitted']
            student.id_proofs_submitted = student_data['id_proofs_submitted']
            student.guardian_name = student_data['guardian_name']
            student.relationship = student_data['relationship']
            student.guardian_mobile_number = student_data['guardian_mobile_number']
            student.save()
            res = {
                'result': 'ok',
            }
            status = 200
        except Exception as Ex:
            res = {
                'result': 'error',
                'message': str(Ex)
            }
            status = 500
        response = simplejson.dumps(res)
        return HttpResponse(response, status=status, mimetype='application/json')

class DeleteStudentDetails(View):
    def get(self, request, *args, **kwargs):
        student_id = kwargs['student_id']       
        student = Student.objects.filter(id=student_id)                          
        student.delete()
        return HttpResponseRedirect(reverse('list_student'))

class EnquiryView(View):

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            res = {
                'result': 'ok',
            }
            response = simplejson.dumps(res)
            return HttpResponse(response, status=200, mimetype='application/json')
        return render(request, 'enquiry.html', {})

    def post(self, request, *args, **kwargs):

        
        if request.is_ajax():
            enquiry_details = ast.literal_eval(request.POST['enquiry'])
            if enquiry_details:
                enquiry = Enquiry()
                enquiry.student_name = enquiry_details['student_name']
                enquiry.address = enquiry_details['address']
                enquiry.mobile_number = enquiry_details['mobile_number']
                enquiry.email = enquiry_details['email']
                enquiry.details_about_clients_enquiry = enquiry_details['details_about_clients_enquiry']
                enquiry.educational_qualification = enquiry_details['educational_qualification']
                enquiry.land_mark = enquiry_details['land_mark']
                if enquiry_details['course'] != '':
                    course = Course.objects.get(id=enquiry_details['course'])
                    enquiry.course = course
                enquiry.remarks = enquiry_details['remarks']
                enquiry.follow_up_date = datetime.strptime(enquiry_details['follow_up_date'], '%d/%m/%Y')
                enquiry.remarks_for_follow_up_date = enquiry_details['remarks_for_follow_up_date']
                if enquiry_details['discount'] == '':
                    enquiry.discount = 0
                else:
                    enquiry.discount = enquiry_details['discount']
                enquiry.save()
                enquiry.auto_generated_num = 'ENQ' + str(Enquiry.objects.latest('id').id)
                enquiry.save()
            res = {
                'result': 'ok',
                
            }
            response = simplejson.dumps(res)
            return HttpResponse(response, status=200, mimetype='application/json')

class EnquiryDetails(View):

    def get(self, request, *args, **kwargs): 
        if request.is_ajax():
            enquiry_list = []
            enquiry_num = request.GET.get('enquiry_num', '')
            try:
                if enquiry_num :
                    enquiry = Enquiry.objects.get(auto_generated_num=enquiry_num)
                    enquiry_list.append({
                        'student_name': enquiry.student_name,
                        'address': enquiry.address,
                        'mobile_number' : enquiry.mobile_number,
                        'email' : enquiry.email,
                        'details_about_clients_enquiry' : enquiry.details_about_clients_enquiry,
                        'educational_qualification': enquiry.educational_qualification,
                        'land_mark': enquiry.land_mark,
                        'course' : enquiry.course.id,
                        'remarks': enquiry.remarks,
                        'follow_up_date': enquiry.follow_up_date.strftime('%d/%m/%Y') if enquiry.follow_up_date else '',
                        'remarks_for_follow_up_date': enquiry.remarks_for_follow_up_date,
                        'discount': enquiry.discount,
                        'auto_generated_num': enquiry.auto_generated_num,
                    })
            except Exception as ex:
                print str(ex), 'Exception'
                enquiry_list = []
            
            response = simplejson.dumps({
                'enquiry': enquiry_list,
            })    
            return HttpResponse(response, status=200, mimetype='application/json')
class SearchEnquiry(View):

    def get(self, request, *args, **kwargs):
        student_name = request.GET.get('student_name', '')
        enquiries = []
        q_list = []
        if student_name :
            enquiries = Enquiry.objects.filter(student_name__icontains=student_name)
            count = enquiries.count()
        else :
            enquiries = []
            count = 0
        enquiry_list = []
        for enquiry in enquiries:
            enquiry_list.append({
                'student_name': enquiry.student_name,
                'address': enquiry.address,
                'mobile_number' : enquiry.mobile_number,
                'email' : enquiry.email,
                'details_about_clients_enquiry' : enquiry.details_about_clients_enquiry,
                'educational_qualification': enquiry.educational_qualification,
                'land_mark': enquiry.land_mark,
                'course' : enquiry.course.name,
                'remarks': enquiry.remarks,
                'follow_up_date': enquiry.follow_up_date.strftime('%d/%m/%Y') if enquiry.follow_up_date else '',
                'remarks_for_follow_up_date': enquiry.remarks_for_follow_up_date,
                'discount': enquiry.discount,
                'auto_generated_num': enquiry.auto_generated_num,
                })
        if request.is_ajax():
            
            response = simplejson.dumps({
                'enquiries': enquiry_list,
                'count': count,
            })    
            return HttpResponse(response, status=200, mimetype='application/json')
        
class StudentAdmission(View):

    def get(self, request, *args, **kwargs):

        return render(request, 'admission_details.html', {})

