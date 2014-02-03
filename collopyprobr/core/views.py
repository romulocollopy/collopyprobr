#coding: utf-8 

from django.shortcuts import render
from collopyprobr.core.fakecontent import contact, about, post

def about(request):
    template_name = "core/about.html"
    context = {"about": about}
    return render(request, template_name, context, content_type="text/html")

def contact(request):
    template_name = "core/contact.html"
    context = {"contact": contact}
    return render(request, template_name, context, content_type="text/html")

def homepage(request):
    template_name = "core/index.html"
    context = {"post": post}
    return render(request, template_name, context, content_type="text/html")
