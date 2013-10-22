from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from dataminas.models import Point

@dajaxice_register
def alertar(request, pk):
    point = Point.objects.get(pk=pk)
    point.user_score += 1
    point.save()
    return simplejson.dumps({'message':'Done!'})
