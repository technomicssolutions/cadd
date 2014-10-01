import sys
import simplejson
import ast
from django.core.urlresolvers import reverse
from django.views.generic.base import View
from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect

from college.models import Software, Course, Batch


class Softwares(View):

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            software_list = []
            softwares = Software.objects.all()
            for software in softwares:
                software_list.append({
                    'id': software.id,
                    'name': software.name,
                    })
            res = {
                'softwares': software_list,
            }
            status = 200
            response = simplejson.dumps(res)
            return HttpResponse(response, status=status, mimetype='application/json')
        return render(request, 'list_softwares.html', {})

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            software_details = ast.literal_eval(request.POST['software_details'])
            try:
                if software_details.get('id'):
                    software = Software.objects.get(id=software_details['id'])
                else:
                    software = Software()
                software.name = software_details['name']
                software.save()
                res = {
                    'result': 'ok',
                    }
            except Exception as ex:
                print str(ex)
                res = {
                    'result': 'error',
                    'message': 'Software Already Exists',
                }
            status_code = 200
            response = simplejson.dumps(res)
            return HttpResponse(response, status = status_code, mimetype="application/json")


class DeleteSoftware(View):

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            try:
                software = Software.objects.get(id=kwargs['software_id'])
                if software.course_set.all().count() > 0 or software.batch_set.all().count() > 0:
                    res = {
                        'result': 'ok',
                        'message': 'This software is currently being used, So cannot delete.'
                    }
                else:
                    name = software.name
                    software.delete()
                    res = {
                        'result': 'ok',
                        'message': name + ' Deleted Successfully',
                    }
            except:
                res = {
                    'result': 'error',
                    'message': 'failed',
                }

            status_code = 200
            response = simplejson.dumps(res)
            return HttpResponse(response, status = status_code, mimetype="application/json")


class Courses(View):

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            course_list = []
            software_list = []
            courses = Course.objects.all()
            for course in courses:
                softwares = course.software.all()
                for software in softwares:
                    software_list.append({
                        'id': software.id,
                        'name': software.name,
                    })
                course_list.append({
                    'id': course.id,
                    'name': course.name,
                    'duration': course.duration,
                    'amount': course.amount,
                    'softwares': software_list,
                })
                software_list = []
            res = {
                'courses': course_list,
            }
            status = 200
            response = simplejson.dumps(res)
            return HttpResponse(response, status=status, mimetype='application/json')
        return render(request, 'list_courses.html', {})        

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            course_details = ast.literal_eval(request.POST['course_details'])
            try:
                if course_details.get('id'):
                    course = Course.objects.get(id=course_details['id'])
                else:
                    course = Course()
                course.name = course_details['name']
                course.save()
                res = {
                    'result': 'ok',
                    }
            except Exception as ex:
                print str(ex)
                res = {
                    'result': 'error',
                    'message': 'Course Already Exists',
                }
            status_code = 200
            response = simplejson.dumps(res)
            return HttpResponse(response, status = status_code, mimetype="application/json")


class ListBatch(View):
    def get(self, request, *args, **kwargs):

        batches = Batch.objects.all()
        batch_list = []
        if request.is_ajax():
            for batch in batches:
                batch_list.append({
                    'software':batch.software.name,
                    'batch_start':batch.start_date,
                    'batch_end':batch.end_date,
                    'allowed_students':batch.allowed_students,                                        
                    'name': batch.name,
                })
            res = {
                'result': 'ok',
                'batches': batch_list,
            }            
            response = simplejson.dumps(res)
            return HttpResponse(response, status=200, mimetype='application/json')
        ctx = {
            'batches': batches
        }
        return render(request, 'batch.html',ctx)


class EditBatch(View): 

    def get(self, request, *args, **kwargs):
        batch_id = kwargs['batch_id']
        context = {
            'batch_id': batch_id,
        }
        ctx_data = []
        if request.is_ajax():
            try:
                batch = Batch.objects.get(id = batch_id)
                ctx_data.append({
                    'software':batch.software.name,
                    'batch_start':batch.start_date,
                    'batch_end':batch.end_date,
                    'allowed_students':batch.allowed_students,                                        
                    'name': batch.name,
                })
                res = {
                    'result': 'ok',
                    'batch': ctx_data,
                }
                status = 200
            except Exception as ex:
                print "Exception == ", str(ex)
                res = {
                    'result': 'error: ' + str(ex),
                    'batch': ctx_data,
                }
                status = 200
            response = simplejson.dumps(res)
            return HttpResponse(response, status=status, mimetype='application/json')
        return render(request, 'edit_batch.html',context)

    def post(self, request, *args, **kwargs):        
        batch_id = kwargs['batch_id']
        batch = Batch.objects.get(id = batch_id)
        data = ast.literal_eval(request.POST['batch'])
        try:
            batch.start_date = data['batch_start']
            batch.end_date = data['batch_end']
            batch.periods = data['batch_periods']
            batch.save()
            res = {
                'result': 'ok',
            }
            status = 200
        except Exception as Ex:
            print "Exception == ", str(Ex)
            res = {
                'result': 'error: '+ str(Ex),
                'message': 'Batch with this name is already existing'
            }
            status = 500
        response = simplejson.dumps(res)
        return HttpResponse(response, status=status, mimetype='application/json')


class AddNewBatch(View):
    def post(self, request, *args, **kwargs):
        status_code = 200
        if request.is_ajax():
            try:
                batch = ast.literal_eval(request.POST['batch'])
                software = Software.objects.get(id = batch['software'])
                batch, created = Batch.objects.get_or_create(software=software, start_time=batch['start'],end_time=batch['end'], allowed_students=batch['allowed_students'], name=batch['name'])
                if not created:
                    res = {
                        'result': 'error',
                        'message': 'Batch already exist'
                    }
                else:
                    batch.save()
                    res = {
                        'result': 'ok',
                        'batch': {
                            'software':batch.software.name,
                            'batch_start':batch.start_date,
                            'batch_end':batch.end_date,
                            'allowed_students':batch.allowed_students,                                        
                            'name': batch.name,
                        }
                    }  
            except Exception as ex:
                res = {
                        'result': 'error: '+ str(ex),
                        'message': 'Batch Name already exist'
                    }
            response = simplejson.dumps(res)
            return HttpResponse(response, status = status_code, mimetype="application/json")
