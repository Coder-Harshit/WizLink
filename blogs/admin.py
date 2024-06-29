from django.contrib import admin
from .models import BlogPost, Comment, Like, Tag, AdminLabel

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Tag)
admin.site.register(AdminLabel)