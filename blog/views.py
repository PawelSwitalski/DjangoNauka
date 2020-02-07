from django.shortcuts import render
# Create your views here.
from .models import Post



def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/blog.html', context) 

def about(request):
	return render(request, 'blog/about.html', {'title': 'about'})
	#return HttpResponse('<h1>Blog about</h1>')