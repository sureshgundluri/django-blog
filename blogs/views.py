from django.shortcuts import get_object_or_404 , render,redirect
from django.http import HttpResponse
from .models import *
from django.db.models import Q
# Create your views here.

def post_by_category(request,category_id):
    # fetch all the post based on the category that we get from the category_id
    posts = Blog.objects.filter(status='Published',category=category_id)
    # User try /except when we want to do custom action if the category doesnot exists
    try:
        category = Category.objects.get(pk=category_id)
    except:
        # redirecting to the home page when category doesnot exists
        return redirect('home')
    # Use get_object_or_404 when you want to see the error page  if the category doesnot exists 
    # category = get_object_or_404(Category,pk=category_id)
    context = {
        'posts':posts,
        'category':category,
    } 
    return render(request,'post_by_category.html',context)


def blogs(request,slug):
    single_blog = get_object_or_404(Blog,slug=slug,status='Published')
    context = {
        'single_blog':single_blog,
    }
    return render(request,'blogs.html',context)

def search(request):
    keyword = request.GET.get('keyword')
    

    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) |Q(blog_body__icontains=keyword),status='Published')
    context = {
        'blogs':blogs,
        'keyword':keyword
    }
    return render(request,'search.html',context)
