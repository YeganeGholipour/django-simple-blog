from django.contrib import admin
from .models import Post, Category

# This allows our blog posts be accessable from the admin area
admin.site.register(Post)
admin.site.register(Category)
