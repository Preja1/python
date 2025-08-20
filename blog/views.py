from django.shortcuts import render
from blog.models import Blog
# Create your views here.
def index_page(request):
    #process here
    return render(request,"index.html")

def blogs_page(request):
    #Django ORM features
    blogs= Blog.objects.all()#Fetch all blogs data
    context ={
        "objects":blogs,
    }

    return render(request,"blogs.html",context)

def blog_detail_page(request,pk):
    #Django ORM features
    blog= Blog.objects.get(id=pk)#Fetch all blogs data
    context ={
        "object":blog,
    }

    return render(request,"blog-detail.html",context)

#MVT