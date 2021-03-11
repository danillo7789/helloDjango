from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homePageView(request):
    return HttpResponse('Hello World!')

def dashboardView(request):
    return HttpResponse('you are on the dashboard')

def authorPage(request):
    return HttpResponse('here are the list of authors')

def postPage(request):
    return HttpResponse('here are your posts')

