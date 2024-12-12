from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

# Create your views here.

def members(request):
    return HttpResponse("Hello world!")

def index_views(request):
    template = loader.get_template('./MDA/index.html')
    return HttpResponse(template.render())

# Prepare Template 

def member_views(request):
    new_data = Member.objects.all().values()
    template = loader.get_template('./MDA/index.html')
    context = {
        'new_data':new_data,
    }

    return HttpResponse(template.render(context, request))