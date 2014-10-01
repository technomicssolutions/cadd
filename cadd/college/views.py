import sys
import simplejson
import ast
from django.core.urlresolvers import reverse
from django.views.generic.base import View
from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect



class ListSoftwares(View):

	def get(self, request, *args, **kwargs):
    
    		return render(request, 'college/list_softwares.html', {})


