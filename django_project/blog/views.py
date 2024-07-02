from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
	print("Home accessed")
	return HttpResponse('<h1>Blog Home</h1>')

def about(request):
	print("About accessed")
	return HttpResponse('<h1>About</h1>')
