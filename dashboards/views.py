from django.shortcuts import render,redirect,get_object_or_404
from blogs.models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# Create your views here.


@login_required(login_url='login')
def dashboards(request):
    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()
    print(category_count)
    print(blogs_count)
    context = {
        'category_count':category_count,
        'blogs_count':blogs_count,
    }
    return render(request,'dashboards/dashboards.html',context)

def categories(request):
    return render(request,'dashboards/categories.html')

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
        else:
            print(form.errors)
    else:
        form = CategoryForm()
    context = {
        'form':form,
    }
    return render(request,'dashboards/add_category.html',context)
def edit_category(request,pk):
    category = get_object_or_404(Category,pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm(instance=category)
    
    context = {
        'form': form,
        'category':category
    }
    
    
    return render(request,'dashboards/edit_category.html',context)

def delete_category(request,pk):
    category = get_object_or_404(Category,pk=pk)
    category.delete()
    return redirect('categories')

def posts(request):
    posts = Blog.objects.all()
    context = {
        'posts':posts,
    }
    return render(request,'dashboards/posts.html',context)

def add_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + "-" + str(post.id)
            post.save()
            return redirect('posts')
    form = BlogPostForm()
    context = {
        'form':form,
    }
    return render(request,'dashboards/add_post.html',context)

def edit_post(request,pk):
    post = get_object_or_404(Blog,pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts')
    else:
        form = BlogPostForm(instance=post)
    
    context = {
        'form': form,
        'post':post,
    }

    return render(request,'dashboards/edit_post.html',context)

def delete_post(request,pk):
    post = get_object_or_404(Blog,pk=pk)
    post.delete()
    return redirect('posts')


def users(request):
    users = User.objects.all()
    context ={
        'users':users,
    }
    return render(request,'dashboards/users.html',context)

def add_user(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user')
    form = AddUserForm()
    context ={
        'form':form,
    }
    return render(request,'dashboards/add_user.html',context)

def edit_user(request,pk):
    user = get_object_or_404(User,pk=pk)
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user')
    else:
        form = EditUserForm(instance=user)
    
    context = {
        'form': form,
        'user':user,
    }

    return render(request,'dashboards/edit_user.html',context)

def delete_user(request,pk):
    user = get_object_or_404(User,pk=pk)
    user.delete()
    return redirect('user')




