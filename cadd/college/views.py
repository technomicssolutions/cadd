import sys
import simplejson
import ast
from django.core.urlresolvers import reverse
from django.views.generic.base import View
from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect

from college.models import Software


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
            response = simplejson.dumps(res)
            return HttpResponse(response, status=status, mimetype='application/json')
        return render(request, 'list_softwares.html', {})


