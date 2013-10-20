# Create your views here.
from django.http import HttpResponse
from dataminas.models import *
from django.shortcuts import render_to_response
from django.template import RequestContext
import datetime

def home(request):
    p = Point(x=datetime.datetime.now(), y=100)
    #p.save()
    html = "<html><body>Point x={0}, y={1} saved</body></html>".format(p.x,p.y)
    return render_to_response('dataminas/home.html', context_instance=RequestContext(request))
