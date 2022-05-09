from django.shortcuts import render
from .models import Post

# Create your views here.

# A view function is a function that takes a request and returns a response. It's a request handler.
# request -> response


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
