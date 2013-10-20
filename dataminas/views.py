# Create your views here.
from django.http import HttpResponse
from dataminas.models import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from dataminas.models import Category,Point
import datetime

def home(request):
    return render_to_response('dataminas/home.html', context_instance=RequestContext(request))

def show_subcategory(request, category, subcategory):
    categories = []
    categories.append(get_object_or_404(Category, name_url=category))
    categories.append(get_object_or_404(Category, name_url=subcategory))

    # Get points
    points = Point.objects.filter(category=categories[-1])

    # Define anomaly
    for point in points:
        if point.algorithm_score > 50 or point.user_score > 0:
            point.anomaly = "true"
        else:
            point.anomaly = "false"

    # Get subcategories
    subcategories = Category.objects.filter(parent=categories[0])
    return render_to_response('dataminas/show_subcategory.html', { 'categories': categories, 'subcategories': subcategories,  'points': points }, context_instance=RequestContext(request))

def show_category(request, category):
    categories = [get_object_or_404(Category, name_url=category)]
    print categories[0].name

    # Get points
    points = Point.objects.filter(category=categories[0])

    # Define anomaly
    for point in points:
        if point.algorithm_score > 50 or point.user_score > 0:
            point.anomaly = "true"
        else:
            point.anomaly = "false"

    # Get subcategories
    subcategories = Category.objects.filter(parent=categories[0])
    return render_to_response('dataminas/show_category.html', { 'categories': categories, 'subcategories': subcategories,  'points': points }, context_instance=RequestContext(request))

def show_point(request, pk):
    point = get_object_or_404(Point, pk=pk)

    return render_to_response('dataminas/show_point.html', { 'point': point }, context_instance=RequestContext(request))

