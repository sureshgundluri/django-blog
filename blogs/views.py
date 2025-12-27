from django.shortcuts import get_object_or_404 , render,redirect
from django.http import HttpResponse,HttpResponseRedirect
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
    if request.method == 'POST':
        comment = Comments()
        comment.user = request.user
        comment.blog = single_blog
        #  getting the comment from the Name parameter of the comment form in the blogs UI.
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info) 
    comments = Comments.objects.filter(blog=single_blog)
    comments_counts = comments.count()
    context = {
        'single_blog':single_blog,
        'comments':comments,
        'comments_counts':comments_counts,
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
