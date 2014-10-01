import sys
import simplejson
import ast
from django.core.urlresolvers import reverse
from django.views.generic.base import View
from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect

from college.models import Software, Batch


class ListSoftwares(View):

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


class ListBatch(View):
    def get(self, request, *args, **kwargs):

        batches = Batch.objects.all()
        
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
                    'branch':batch.branch.branch if batch.branch else '',                  
                    'batch_start':batch.start_date,
                    'batch_end':batch.end_date,
                    'batch_periods':batch.periods,                                        
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
        return render(request, 'college/edit_batch.html',context)

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
                course = Course.objects.get(id = request.POST['course'])
                if request.POST['branch']:
                    branch = CourseBranch.objects.get(id = request.POST['branch'])
                    batch, created = Batch.objects.get_or_create(course=course, start_date=request.POST['batch_start'],end_date=request.POST['batch_end'],periods=request.POST['periods'],branch=branch)
                else:
                    batch, created = Batch.objects.get_or_create(course=course, start_date=request.POST['batch_start'],end_date=request.POST['batch_end'],periods=request.POST['periods'])
                if not created:
                    res = {
                        'result': 'error',
                        'message': 'Batch already exist'
                    }
                else:
                    batch.save()
                    res = {
                        'result': 'ok',
                    }  
            except Exception as ex:
                print str(ex), "Exception ===="
                res = {
                        'result': 'error: '+ str(ex),
                        'message': 'Batch Name already exist'
                    }
            response = simplejson.dumps(res)
            return HttpResponse(response, status = status_code, mimetype="application/json")
