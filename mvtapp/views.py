from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def detail(request):
    return  HttpResponse('response detail')
