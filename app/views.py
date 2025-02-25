from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages

from django.urls import reverse

from app.models import Blog
from .forms import BlogForm, CommentForm


def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs': blogs})


@login_required(login_url='/login/')
def create_blog(request):
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if not request.user.is_authenticated:
            messages.warning(request, 'Avval login qiling')
            return redirect(reverse('app:create'))
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
        return redirect(reverse('app:home'))

    context = {'form': form}
    return render(request, 'create_blog.html', context)


def detail_blog(request, id):
    blog = get_object_or_404(Blog, id=id)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.author = request.user
            comment.save()
            return redirect('app:detail', blog.id)
    context = {
        "blog": blog,
        "form": form,
    }
    return render(request, 'detail_blog.html', context)


#
@login_required(login_url='/login/')
def edit_blog(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    if request.user != blog.author:
        messages.warning(request, 'Bu blog sizga tegishli emas!')
        return redirect('app:login')
    form = BlogForm(instance=blog)
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if not request.user.is_authenticated:
            messages.warning(request, 'Avval login qiling')
            return redirect(reverse('app:create'))
        if form.is_valid():
            blog = form.save()
            return redirect('app:detail', blog.id)
    context = {
        'form': form,
        'blog': blog,
    }
    return render(request, 'edit_blog.html', context)
