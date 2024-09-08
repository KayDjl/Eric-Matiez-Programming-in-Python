from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
# Create your views here.


def index(request):
    index = BlogPost.objects.order_by('-date_added')
    context = {'index': index}
    return render(request, 'blogs/index.html', context)

@login_required
def new_blog(request):
    
    if request.method != 'POST':
        form = BlogForm()
    else:
        form = BlogForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.owner = request.user
            user.save()
            return redirect('blogs:index')
        
    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)

@login_required
def edit_blog(request, blog_id):
    blog = BlogPost.objects.get(id=blog_id)
    if blog.owner != request.user:
        raise Http404
    
    if request.method != 'POST':
        form = BlogForm(instance=blog)
    else:
        form = BlogForm(instance=blog, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')
    context = {'blog': blog, 'form': form}
    return render(request, 'blogs/edit_blog.html', context)