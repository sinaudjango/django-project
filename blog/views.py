from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request):
    post = Post.objects.all();
    categories = Post.objects.values('category').distinct();
    print(categories);
    context = {
        'judul': 'Kelas Terbuka',
        'postingIndex':post,
        'categoriesIndex':categories,
    }
    return render(request, 'blog/index.html', context)

def slugPost(request, slugInput):
    post = Post.objects.get(slug=slugInput);
    categories = Post.objects.values('category').distinct();
    context = {
        'judul': 'Kelas Terbuka',
        'postingDetails':post,
        'categoriesIndex': categories,
    }
    return render(request, 'blog/blog-details.html', context)

def categoryPost(request, categoryInput):
    postCat = Post.objects.filter(category=categoryInput);
    categories = Post.objects.values('category').distinct();
    print(categories);
    context = {
        'test': 'test',
        'postingIndex': postCat,
        'categoriesIndex': categories,
    }
    return render(request, 'blog/index.html', context)
