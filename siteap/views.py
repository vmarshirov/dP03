from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("siteapПривет")

def abc(request):
    return HttpResponse('siteapabc')