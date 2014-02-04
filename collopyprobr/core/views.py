#coding: utf-8 

from django.shortcuts import render
from collopyprobr.core.fakecontent import contact, about, history 

def aboutpage(request):
    template_name = "core/about.html"
    dictionary = {"about": about}
    return render(request, template_name, dictionary, content_type="text/html")

def contactpage(request):
    template_name = "core/contact.html"
    dictionary = {"contact": contact}
    return render(request, template_name, dictionary, content_type="text/html")

def homepage(request):
    template_name = "core/index.html"
    dictionary = {"history": history}
    return render(request, template_name, dictionary, content_type="text/html")
