# Create your views here.
from django.http import HttpResponse
from dataminas.models import *
from django.shortcuts import render_to_response
from django.template import RequestContext
import datetime

def home(request):
    return render_to_response('dataminas/home.html', context_instance=RequestContext(request))
