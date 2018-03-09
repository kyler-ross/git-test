from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class aboutpageview(TemplateView):
    template_name = 'about.html'

class project1pageview(TemplateView):
    template_name = 'Week1_ProjectA.html'

class project2pageview(TemplateView):
    template_name = 'Week2_ProjectB.html'

class project3pageview(TemplateView):
    template_name = 'Week3_ProjectC.html'