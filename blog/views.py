from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def kishore(request):
    return HttpResponse('<h1><marquee>kishore is a good boy</marquee></h1>')

def kumar(request):
    return HttpResponse('<h1><marquee>kumar trusts blindly</marquee></h1>')