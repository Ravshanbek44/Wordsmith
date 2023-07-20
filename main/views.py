from django.http import HttpResponse
from django.shortcuts import render
from .models import Post, Comment, Tag, Category, Contact, Banner
from .forms import ContactForm, CommentForm


def index(request):
    post = Post.objects.all()
    banner = Banner.objects.all()
    category = Category.objects.all()

    ctx = {
        'posts': post,
        'banners': banner,
        'category': category
    }
    return render(request, 'index.html', ctx)


def detailpage(request, pk):
    form = CommentForm()
    blog = Post.objects.get(id=pk)
    comment = Comment.objects.filter(post=blog)
    if request.method == "POST":
        if form.is_valid():
            form.save()
    ctx = {
        'blog': blog,
        'form': form,
        'comments': comment
    }
    return render(request, 'single-standard.html', ctx)


def contactpage(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, 'page-contact.html', context)
