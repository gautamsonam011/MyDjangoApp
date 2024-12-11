from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def members(request):
    return HttpResponse("Hello world!")

def index_views(request):
    template = loader.get_template('./MDA/index.html')
    return HttpResponse(template.render())