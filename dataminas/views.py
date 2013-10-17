# Create your views here.
from django.http import HttpResponse
from dataminas.models import *
import datetime

def start(request):
    p = Point(x=datetime.datetime.now(), y=100)
    p.save()
    html = "<html><body>Point x={0}, y={1} saved</body></html>".format(p.x,p.y)
    return HttpResponse(html)
