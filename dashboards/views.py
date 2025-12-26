from django.shortcuts import render,redirect,get_object_or_404
from blogs.models import *
from django.contrib.auth.decorators import login_required
from .forms import *
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


