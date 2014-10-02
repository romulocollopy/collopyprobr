#coding: utf-8

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from collopyprobr.core.fakecontent import (
    contact, about, histories)


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
    dictionary = {"history": histories["1"]}
    return render(request, template_name, dictionary, content_type="text/html")


def postdetail(request, id):
    template_name = "core/detail.html"
    dictionary = get_object_or_404(histories, pk=id)
    return render(request, template_name, dictionary, content_type="text/html")
