from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.
def homePageView(request):
    return HttpResponse('Hello World!')

def dashboardView(request):
    return HttpResponse('you are on the dashboard')

def authorPage(request):
    return HttpResponse('here are the list of authors')

def postPage(request):
    return HttpResponse('here are your posts')

class HomePageView(TemplateView):
    template_name="home.html"

class AboutPage(TemplateView):
    template_name="about.html"

