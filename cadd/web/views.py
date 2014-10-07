import simplejson
import ast
from datetime import datetime

from django.views.generic.base import View
from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse

from web.models import Letter


class Home(View):
    def get(self, request, *args, **kwargs):
        
        return render(request, 'home.html',{})# Create your views here.


class Letters(View):
    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            letters_list = []
            letters = Letter.objects.all()
            for letter in letters:
                letters_list.append({
                    'id': letter.id,
                    'date': letter.date.strftime('%d/%m/%Y'),
                    'from': letter.from_address,
                    'to': letter.to_address,
                    'type': letter.letter_type,
                })
            res = {
                'letters' : letters_list,
            }
            response = simplejson.dumps(res)
            return HttpResponse(response, status=200, mimetype="application/json")
        return render(request, 'letter.html',{})
    
    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            letter_details = ast.literal_eval(request.POST['letter_details'])
            try:
                if letter_details.get('id'):
                    letter = Letter.objects.get(id=letter_details['id'])
                else:
                    letter = Letter()
                letter.letter_type = letter_details['type']
                letter.date = datetime.strptime(letter_details['date'], '%d/%m/%Y')
                letter.from_address = letter_details['from']
                letter.to_address = letter_details['to']
                letter.save()
                res = {
                    'result': 'ok',
                    }
            except Exception as ex:
                print str(ex)
                res = {
                    'result': 'error',
                    'message': 'Failed',
                }
            status_code = 200
            response = simplejson.dumps(res)
            return HttpResponse(response, status = status_code, mimetype="application/json")


class DeleteLetter(View):
    def get(self,request,*args,**kwargs):
        letter_id = kwargs['letter_id']
        letter = Letter.objects.get(id=letter_id)
        letter.delete()
        return render(request, 'letter.html', {})




class Login(View):
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('home'))
        return render(request,'home.html',{})

    def post(self,request,*args,**kwargs):
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user and user.is_active:
            login(request, user)
        else:
            context = {
                'message' : 'Username or password is incorrect'
            }
            return render(request, 'home.html',context)
        context = {
         'Success_message': 'Welcome '+request.POST['username']
        }
        return HttpResponseRedirect(reverse('home'))

class Logout(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('home'))

class ResetPassword(View):

    def get(self, request, *args, **kwargs):

        user = User.objects.get(id=kwargs['user_id'])
        context = {
            'user_id': user.id
        }
        return render(request, 'reset_password.html', context)

    def post(self, request, *args, **kwargs):

        context = {}
        user = User.objects.get(id=kwargs['user_id'])
        if request.POST['password'] != request.POST['confirm_password']:
            context = {
                'user_id': user.id,
                'message': 'Password is not matched with Confirm Password',
            }
            return render(request, 'reset_password.html', context)
        if len(request.POST['password']) > 0 and not request.POST['password'].isspace():
            user.set_password(request.POST['password'])
        user.save()
        if user == request.user:
            logout(request)
            return HttpResponseRedirect(reverse('home'))  
        else:
            user_type = user.userprofile_set.all()[0].user_type 
            return HttpResponseRedirect(reverse('users', kwargs={'user_type': user_type}))