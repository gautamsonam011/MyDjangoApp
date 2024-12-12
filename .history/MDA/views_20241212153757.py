from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User

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