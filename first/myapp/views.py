from django.shortcuts import render 
from django.http import HttpResponse 
from django.template import loader 
def home(request): 
    return HttpResponse("home page is displayed") 
def htmlpage(request): 
    template = loader.get_template('tem.html') 
    return HttpResponse(template.render())