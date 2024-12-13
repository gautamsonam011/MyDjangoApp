from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User
from django.db.models import Q

# Create your views here.

def members(request):
    return HttpResponse("Hello world!")

def index_views(request):
    template = loader.get_template('./MDA/index.html')
    return HttpResponse(template.render())

# Prepare Template 

def member_views(request):
    new_data = User.objects.all().values()
    template = loader.get_template('./MDA/index.html')
    context = {
        'new_data':new_data,
    }

    return HttpResponse(template.render(context, request))

def date_details(request, id):
    data = User.objects.get(id=id)
    template = loader.get_template('./MDA/date.html')
    context = {
        'data':data,
    }

    return HttpResponse(template.render(context, request))

# Master Template 

def master_views(request):
    new_data = User.objects.all().values()
    template = loader.get_template('./MDA/allMaster.html')
    context = {
        'new_data':new_data,
    }

    return HttpResponse(template.render(context, request))


# add main index page 

def main_views(request):
    template = loader.get_template('./MDA/home.html')
    return HttpResponse(template.render())

# 404 Not Found 

def not_found(request):
    template = loader.get_template('./MDA/404error.html')
    return HttpResponse(template.render())

# text views 

def testing_views(request):
    template = loader.get_template('./MDA/testing.html')
    context = {
        'fruits': ['Apple', 'Banana', 'Cherry'],
    }

    return HttpResponse(template.render(context, request))

# variables 

def variables_create(request):
    template = loader.get_template('./MDA/home.html')
    context = {
        'fruit': 'Chiku',
    }

    return HttpResponse(template.render(context, request))

# Django QuerySet - Get Data 

# The values() method 

def user_views(request):
    mydata = User.objects.all().values()

    # return specific columns 
    # values_list() 

    data1 = User.objects.values_list('firstName')
    data2 = User.objects.filter(firstName='Sonam').values()

    template = loader.get_template('./MDA/queryset.html')

    context = {
        'data':mydata,
        'data1':data1,
        'data2':data2,
    }

    return HttpResponse(template.render(context, request))

# mydata = User.objects.filter(lastName="Gautam", id=2).values()
# mydata = User.objects.filter(firstName='Sonam').values() | User.objects.filter(firstName='Ankit').values()

def q_views(request):
    mydata = User.objects.filter(Q(firstName='Sonam') | Q(firstName='Ankit')).values()
    template = loader.get_template('./MDA/queryset.html')

    context = {
        'qdata':mydata,
    }

    return HttpResponse(template.render(context, request))

# Field Lookups 

# .filter(firstName__startswith='L')




