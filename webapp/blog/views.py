from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# handle routes

# home page
def home(request):
    return HttpResponse('<h1>Blog Home</h1>')

# about page
def about(request):
    return HttpResponse('<h1>Blog About</h1>')