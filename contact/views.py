from django.shortcuts import render
from .forms import ContactForm
from blog.models import Post
# Create your views here.

def index(request):
    contact_form    = ContactForm()
    categories      = Post.objects.values('category').distinct();
    context         = {
                'judul':'Kelas Terbuka Membuat Form',
                'page': 'Contact Page',
                'categoriesIndex': categories,
                'data_form':contact_form,
    }
    print(request.POST)
    return render(request, 'contact/index.html', context)