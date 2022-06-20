from wsgiref.util import request_uri
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


data="anda melakukan request dengan ke "
def create(request):
    return HttpResponse("anda melakukan request dengan ke {}".format(request.path))

def read(request):
    return HttpResponse("anda melakukan request dengan ke {}".format(request.path))

def update(request):
    return HttpResponse("anda melakukan request dengan ke {}".format(request.path))

def delete(request):
    return HttpResponse("anda melakukan request dengan ke {}".format(request.path))