from django.contrib import admin

# Register your models here.
from blog.models import Blog

admin.site.register(Blog)

from blog.models import Comments

admin.site.register(Comments)