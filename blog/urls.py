from django.urls import path
from blog.views import index_page,blogs_page,blog_detail_page

urlpatterns=[
    path("",index_page),
    path("blogs/",blogs_page),
    path("blog/<str:pk>/",blog_detail_page)
]