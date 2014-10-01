import sys
import simplejson
import ast
from django.core.urlresolvers import reverse
from django.views.generic.base import View
from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect

from college.models import Software, Course


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