
import simplejson
import ast
from datetime import datetime

from django.core.urlresolvers import reverse
from django.views.generic.base import View
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User

from staff.models import Staff, Permission

class AddStaff(View):    
    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            staff_details = ast.literal_eval(request.POST['staff'])
            print staff_details
            if staff_details.get('id', ''):
                staff = Staff.objects.get(id=staff_details['id'])
                user = staff.user
            else:
                try:
                    user = User.objects.get(username=staff_details['username'])
                    res = {
                        'result': 'error',
                        'message': 'Username already exists',
                    }
                except Exception as ex:
                    user = User.objects.create(username=staff_details['username'])
                    user.set_password(staff_details['password'])
                    user.is_staff = True
                    user.save()
                    staff = Staff.objects.create(user=user)
            user.first_name = staff_details['first_name']
            user.last_name = staff_details['last_name']
            user.email = staff_details['email']
            user.save()
            staff.dob = datetime.strptime(staff_details['dob'], '%d/%m/%Y')
            staff.address = staff_details['address']
            staff.mobile_number = staff_details['mobile_number']
            staff.land_number = staff_details['land_number']                
            staff.blood_group = staff_details['blood_group']
            staff.doj = datetime.strptime(staff_details['doj'], '%d/%m/%Y')
            staff.qualifications = staff_details['qualifications']
            staff.photo = request.FILES.get('photo_img', '')
            staff.experience = staff_details['experience']
            staff.role = staff_details['role']
            staff.save()
            res = {
                'result': 'ok',
            }  
            response = simplejson.dumps(res)
            return HttpResponse(response, status=200, mimetype="application/json")

class ListStaff(View):

    def get(self, request, *args, **kwargs):
        
        staffs = Staff.objects.all()
        if request.GET.get('staff_name', ''):
            staffs = Staff.objects.filter(user__first_name__istartswith=request.GET.get('staff_name', ''))
        if request.is_ajax():
            staff_list = []
            for staff in staffs:
                staff_list.append({
                    'id': staff.id,
                    'first_name': staff.user.first_name,
                    'last_name': staff.user.last_name,
                    'username': staff.user.username,
                    'dob': staff.dob.strftime('%d/%m/%Y'),
                    'address': staff.address,
                    'mobile_number' : staff.mobile_number,
                    'land_number' : staff.land_number,
                    'email': staff.user.email,
                    'blood_group': staff.blood_group,
                    'doj': staff.doj.strftime('%d/%m/%Y'),
                    'qualifications': staff.qualifications,
                    'role': staff.role,
                    'experience': staff.experience,
                    'photo': staff.photo.name,
                })
            res = {
                'result': 'Ok',
                'staffs': staff_list
            }
            status = 200
            response = simplejson.dumps(res)
            return HttpResponse(response, status=status, mimetype='application/json')
        return render(request, 'list_staff.html',{})

class DeleteStaffDetails(View):
    def get(self, request, *args, **kwargs):

        staff_id = kwargs['staff_id']       
        staff = Staff.objects.filter(id=staff_id)                          
        staff.delete()
        return HttpResponseRedirect(reverse('staffs'))

class IsUsernameExists(View):

    def get(self, request, *args, **kwargs):

        if request.is_ajax():
            status = 200
            username = request.GET.get('username', '')
            print username , 'username'
            try:
                user = User.objects.get(username=username)
                res = {
                    'result': 'error',
                    'message': 'Username already existing',
                }
            except Exception as ex:
                print "ex == ", str(ex)
                res = {
                    'result': 'ok',
                }
            response = simplejson.dumps(res)
            return HttpResponse(response, status=status, mimetype='application/json')

class PermissionSetting(View):

    def get(self, request, *args, **kwargs):

        return render(request, 'permission_setting.html', {})

    def post(self, request, *args, **kwargs):

        if request.is_ajax():
            permission_details = ast.literal_eval(request.POST['permission_details'])
            staff = Staff.objects.get(id=permission_details['staff'])
            if staff.permission:
                permission = staff.permission
            else:
                permission = Permission()
            res = {
                'result': 'ok',
            }
            response = simplejson.dumps(res)
            return HttpResponse(response, status=200, mimetype='application/json')