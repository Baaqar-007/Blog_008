from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post

def home(request):
	print("Home accessed")
	context = {
		'posts' : Post.objects.all()
	}
	return render(request, 'blog/home.html', context)

def about(request):
	print("About accessed")
	return render(request, 'blog/about.html', {'title':'About'})
