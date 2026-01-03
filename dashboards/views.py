from django.shortcuts import render,redirect,get_object_or_404
from blogs.models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
# Create your views here.


@login_required(login_url='login')
def dashboards(request):
    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()
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
            messages.success(request,"📂 New category added successfully.")
            return redirect('categories')
        else:
            messages.error(request,"❌ Failed to add category. Please check the form.")
            return redirect('categories')
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
            messages.success(request, "✏️ Category updated successfully.")
            return redirect('categories')
        else:
            messages.error(request,"❌ Failed to update category. Please check the form.")
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
    if request.method == 'POST':
        category.delete()
        messages.warning(request,"🗑️ Category deleted successfully.")
        return redirect('categories')
    context ={
        'category':category,
        'cancel':reverse('categories')
    }
    return render(request,'dashboards/confirm_delete.html',context)

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
            messages.success(request,"New Blog Post added successfully."
            )
            return redirect('posts')
        else:
            messages.error(request,"❌ Failed to add Blog Post. Please check the form.")
            return redirect('posts')
    form = BlogPostForm()
    context = {
        'form':form,
    }
    return render(request,'dashboards/add_post.html',context)

def edit_post(request,pk):
    post = get_object_or_404(Blog,pk=pk)
    # 🚫 Permission check AFTER click
    if post.author != request.user:
        messages.warning(
            request,
            "⛔ You don't have permission to edit this blog."
        )
        return redirect('posts')    
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "✏️ Blog Post updated successfully.")
            return redirect('posts')
        else:
            messages.error(request,"❌ Failed to update Blog Post. Please check the form.")
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
    # 🚫 Permission check AFTER click
    if post.author != request.user:
        messages.warning(
            request,
            "⛔ You don't have permission to delete this blog."
        )
        return redirect('posts')
    if request.method == 'POST':
        post.delete()
        messages.warning(request,"🗑️ Blog Post deleted successfully.")
        return redirect('posts')
    context ={
        'post':post,
        'cancel':reverse('posts')
    }
    return render(request,'dashboards/confirm_delete.html',context)
    


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
            messages.success(request,"New Blog Post added successfully.")
            return redirect('user')
        else:
            messages.error(
                request,
                "❌ Failed to add user. Please correct the errors below."
            )
            return redirect('add_user')
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
            messages.success(request,"✏️ User details updated successfully.")
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
    if request.method == 'POST':
        user.delete()
        messages.warning(request,"🗑️ User deleted successfully.")
        return redirect('user')
    context ={
        'user':user,
        'cancel':reverse('user')
    }
    return render(request,'dashboards/confirm_delete.html',context)




