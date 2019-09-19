from django.shortcuts import render
from blog.models import Post
def index(request):
    post = Post.objects.all();
    categories = Post.objects.values('category').distinct();
    context = {
        'judul': 'Kelas Terbuka',
        'postingIndex':post,
        'categoriesIndex': categories,
    }
    return render(request, 'index.html', context)